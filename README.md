# REELS — Ivini reelovi na Macu

Mirkove ideje i iskustvo, složeno kao radni postav za Claude Code na Ivinom
iMacu: od dugih snimki (dron, mobitel) Claude slaže gotove reelove —
kadrovi bez ponavljanja, rezovi u ritmu, glazba iz ElevenLabsa i grafika od
Claudeovog dizajnera. Sve lokalno, bez servera.

| Format | Omjer | Trajanje | Glasnoća | Kodek |
|---|---|---|---|---|
| 1080 × 1920 | 9:16 | 30 s | −12 LUFS | H.264 |

## Sadržaj

- [`CLAUDE.md`](CLAUDE.md) — pravila koja Claude čita na početku svakog rada
- [`upute/postavljanje.md`](upute/postavljanje.md) — što treba i kako postaviti Mac (koraci 1–2)
- [`upute/glazba.md`](upute/glazba.md) — ElevenLabs: ključ, recepti za glazbu, jingle
- [`upute/dizajner.md`](upute/dizajner.md) — poruka dizajneru za logo, natpise i jingle
- [`upute/svaki-dan.md`](upute/svaki-dan.md) — kako naručiti reelove, ispravci, brza pomoć, Hetzner
- [`alati/provjeri_reel.py`](alati/provjeri_reel.py) — automatska provjera gotovog reela

## Struktura mape na Macu

```
~/Reels/
    1 Snimke/     ← duge snimke (dron, mobitel) — originali, ne diraju se
    2 Glazba/     ← glazba iz ElevenLabsa
    3 Grafika/    ← paketi od dizajnera (logo, natpisi, jingle)
    4 Gotovo/     ← gotovi reelovi
```

> Mapa ne smije biti na Desktopu ni u Dokumentima ako su u iCloudu — Mac bi
> svaki video od nekoliko stotina MB slao u iCloud. Mirko je na to naletio.
