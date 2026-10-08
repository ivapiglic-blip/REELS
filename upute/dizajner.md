# Dizajner: logo, natpisi i jingle

Claudeov dizajner (claude.ai) crta animiranu grafiku **preko** videa. Ne radi
video, nego paket (HTML animacija + skripta za render); Claude Code na iMacu
od njega napravi prozirni sloj.

1. Otvori dizajnera, pošalji logo (PNG s prozirnom pozadinom) i poruku ispod.
2. Preuzmi zip i raspakiraj u `3 Grafika/<naziv>`.
3. Claude Codeu: „U ‘3 Grafika/<naziv>’ je novi paket od dizajnera. Pročitaj
   upute, iscrtaj grafiku za 30 s s prozirnom pozadinom, provjeri je i koristi
   je na reelovima.”

## Poruka dizajneru
```text
Trebam animiranu grafiku za vertikalne reelove
(Instagram/Facebook/TikTok), koja ide PREKO videa. Šaljem ti svoj logo.

Format: 1080×1920, 9:16, trajanje 30 s, PROZIRNA pozadina (osim
završnog ekrana).
Vremena:
- 0–1 s: prazno, čisti kadar
- 1–2,4 s: logo i [IME MJESTA / NASLOV] ulaze, ispod sredine kadra
  (oko 60 % visine), da ne smetaju tekstu i gumbima Instagrama
- 2,4–26 s: logo stoji, s blagim pokretom u ritmu
- 26–29 s: jingle — logo se poveća i dođe u sredinu, tamna pozadina u
  mojim bojama
- 29–30 s: statični završni ekran
Natpisi: napravi i zasebnu donju traku (ime osobe + funkcija) koju
mogu staviti bilo kad.
Boje i font: [UPIŠI SVOJE BOJE I FONT, ili "prema logu"].

Predaj mi paket s: HTML animacijom, skriptom za render (puppeteer +
ffmpeg) koja izbacuje ProRes 4444 s alfa kanalom, fontovima u paketu i
kratkim uputama. Mjesto/naslov neka bude parametar (npr. ?grad=Rovinj),
da isti paket radi za sve.
```

Dizajner sam ne može pokrenuti render — to radi Claude Code i provjerava dvije
stvari koje su jednom promakle: **pozadinu koja nije prozirna** i **traku
playera na dnu slike**. Obje su u `CLAUDE.md`, a `alati/provjeri_reel.py
--sloj` provjerava alfa kanal.
