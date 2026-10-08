#!/usr/bin/env python3
"""Provjera gotovog reela (ili prozirnog sloja grafike) prema pravilima iz CLAUDE.md.

Upotreba:
    python3 alati/provjeri_reel.py "4 Gotovo/reel1.mp4" [--trajanje 30]
    python3 alati/provjeri_reel.py "3 Grafika/Moj logo/sloj.mov" --sloj

Treba ffmpeg i ffprobe. Izlazni kod 1 ako postoji ijedna GREŠKA.
"""
import argparse
import json
import re
import subprocess
import sys

TOLERANCIJA_S = 0.1      # koliko smiju odstupati slika, zvuk i zadano trajanje
CILJ_LUFS = -12.0
TOLERANCIJA_LUFS = 1.5


def ffprobe(put):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-print_format", "json",
         "-show_format", "-show_streams", put],
        capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(out)


def trajanje_streama(s, fmt):
    for kljuc in (s.get("duration"), s.get("tags", {}).get("DURATION")):
        if not kljuc:
            continue
        if ":" in kljuc:
            h, m, sek = kljuc.split(":")
            return int(h) * 3600 + int(m) * 60 + float(sek)
        return float(kljuc)
    return float(fmt.get("duration", 0))


def glasnoca(put):
    err = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", put,
         "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    nalazi = re.findall(r"I:\s+(-?[\d.]+) LUFS", err)
    return float(nalazi[-1]) if nalazi else None


def alfa_je_prozirna(put, trenutak):
    """Vraća najmanju alfa vrijednost kadra (0–255) ili None ako nema alfe."""
    err = subprocess.run(
        ["ffmpeg", "-hide_banner", "-ss", str(trenutak), "-i", put,
         "-frames:v", "1", "-vf", "alphaextract,signalstats,metadata=print",
         "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    m = re.search(r"lavfi\.signalstats\.YMIN=(\d+)", err)
    return int(m.group(1)) if m else None


def provjeri_reel(put, info, zadano, greske, upozorenja):
    fmt = info["format"]
    video = [s for s in info["streams"] if s["codec_type"] == "video"]
    audio = [s for s in info["streams"] if s["codec_type"] == "audio"]
    if not video:
        greske.append("nema video streama")
        return
    v = video[0]

    if (v.get("width"), v.get("height")) != (1080, 1920):
        greske.append(f"rezolucija {v.get('width')}×{v.get('height')}, treba 1080×1920")
    if v.get("codec_name") != "h264":
        greske.append(f"video kodek {v.get('codec_name')}, treba H.264")
    elif v.get("profile") != "High":
        upozorenja.append(f"H.264 profil {v.get('profile')}, preporučeno High")

    fps_br, fps_naz = (int(x) for x in v.get("avg_frame_rate", "0/1").split("/"))
    fps = fps_br / fps_naz if fps_naz else 0
    if not any(abs(fps - f) < 0.05 for f in (25, 30)):
        upozorenja.append(f"{fps:.2f} fps, očekivano 25 ili 30")

    t_slika = trajanje_streama(v, fmt)
    if abs(t_slika - zadano) > TOLERANCIJA_S:
        greske.append(f"slika traje {t_slika:.2f} s, traženo {zadano:g} s")

    if not audio:
        greske.append("nema zvuka")
    else:
        a = audio[0]
        t_zvuk = trajanje_streama(a, fmt)
        if abs(t_slika - t_zvuk) > TOLERANCIJA_S:
            greske.append(f"slika {t_slika:.2f} s, zvuk {t_zvuk:.2f} s — ne traju jednako")
        if a.get("codec_name") != "aac":
            greske.append(f"audio kodek {a.get('codec_name')}, treba AAC")
        if a.get("sample_rate") != "48000":
            greske.append(f"audio {a.get('sample_rate')} Hz, treba 48 kHz")
        br = int(a.get("bit_rate") or 0)
        if br and br < 240_000:
            upozorenja.append(f"audio {br // 1000} kb/s, preporučeno 256 kb/s")
        lufs = glasnoca(put)
        if lufs is None:
            upozorenja.append("glasnoću nije moguće izmjeriti")
        elif abs(lufs - CILJ_LUFS) > TOLERANCIJA_LUFS:
            greske.append(f"glasnoća {lufs:.1f} LUFS, cilj {CILJ_LUFS:g} LUFS")

    with open(put, "rb") as f:
        glava = f.read(2 * 1024 * 1024)
    moov, mdat = glava.find(b"moov"), glava.find(b"mdat")
    if moov == -1 or (mdat != -1 and moov > mdat):
        greske.append("nije +faststart (moov nije na početku datoteke)")

    tagovi = {k.lower() for k in fmt.get("tags", {})}
    tagovi -= {"major_brand", "minor_version", "compatible_brands", "encoder"}
    if tagovi:
        greske.append("ostali metapodaci (" + ", ".join(sorted(tagovi))
                      + ") — skini ih s -map_metadata -1")
    if b"c2pa" in glava.lower() or b"jumbf" in glava.lower():
        greske.append("pronađen C2PA/JUMBF zapis — Facebook će staviti oznaku „AI sadržaj”")


def provjeri_sloj(put, info, zadano, greske, upozorenja):
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    if v is None:
        greske.append("nema video streama")
        return
    if (v.get("width"), v.get("height")) != (1080, 1920):
        greske.append(f"rezolucija {v.get('width')}×{v.get('height')}, treba 1080×1920")
    pix = v.get("pix_fmt", "")
    if "a" not in pix.replace("yuv", "").replace("gbr", ""):
        greske.append(f"format piksela {pix} nema alfa kanal — sloj bi prekrio video")
        return
    t = trajanje_streama(v, info["format"])
    if abs(t - zadano) > TOLERANCIJA_S:
        greske.append(f"sloj traje {t:.2f} s, traženo {zadano:g} s")
    # 0–1 s mora biti prazno, a sredina mora biti uglavnom prozirna.
    for trenutak in (0.5, zadano / 2):
        najmanja = alfa_je_prozirna(put, trenutak)
        if najmanja is None:
            upozorenja.append(f"alfu u {trenutak:g} s nije moguće pročitati")
        elif najmanja > 0:
            greske.append(f"u {trenutak:g} s nijedan piksel nije proziran "
                          "— pozadina nije prozirna")
    upozorenja.append("ručno pogledaj dno kadra: ne smije biti trake playera")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("datoteka")
    p.add_argument("--trajanje", type=float, default=30.0, help="traženo trajanje u s (zadano 30)")
    p.add_argument("--sloj", action="store_true", help="provjeri prozirni sloj grafike umjesto reela")
    a = p.parse_args()

    info = ffprobe(a.datoteka)
    greske, upozorenja = [], []
    (provjeri_sloj if a.sloj else provjeri_reel)(a.datoteka, info, a.trajanje, greske, upozorenja)

    for g in greske:
        print(f"GREŠKA: {g}")
    for u in upozorenja:
        print(f"Upozorenje: {u}")
    if not greske:
        print("U redu.")
    sys.exit(1 if greske else 0)


if __name__ == "__main__":
    main()
