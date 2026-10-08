# Postavljanje

## Što treba
- **iMac M5** — dovoljno brz da reel od 30 s složi za manje od minute.
- **Claude pretplata** Pro ili Max (za svakodnevni rad s videom Max, više kvote).
- **ElevenLabs račun** — za objavljene/prodane reelove paket s komercijalnom upotrebom.
- **~50 GB slobodnog diska.**
- Server (Hetzner) **ne treba**.

## Korak 1 — Claude i mapa
1. Preuzmi Claude za Mac: claude.ai/download, prijavi se.
2. Napravi mapu `Reels` u osobnoj mapi (Finder → Idi → Početna), ne na Desktopu.
3. Unutra četiri podmape: `1 Snimke`, `2 Glazba`, `3 Grafika`, `4 Gotovo`.

## Korak 2 — prva poruka (Claude sam postavi alate)
U aplikaciji Claude → kartica **Code** → odaberi mapu `Reels` → zalijepi:

```text
Bok! Ja sam Iva i radim reelove (Instagram, Facebook, TikTok) od dugih
snimki. Imam iMac M5. Molim te postavi sve što trebaš za rad s videom na
ovom Macu:
1. Provjeri postoje li Homebrew, ffmpeg, Python 3 i Node. Što fali,
instaliraj. Ako za nešto treba moja lozinka za Mac, reci mi točno što da
upišem u Terminal, pa ću to napraviti sama.
2. Instaliraj Python pakete pillow i numpy, i puppeteer za Node (trebat
će za grafiku od dizajnera).
3. U ovoj mapi napravi datoteku CLAUDE.md s pravilima koja ću ti
zalijepiti u sljedećoj poruci.
Na kraju mi kratko javi što je instalirano i radi li sve. Piši mi na
hrvatskom.
```

Lozinka za Mac (samo za Homebrew) upisuje se **samo u Terminal**, nikad u razgovor.

## Korak 3 — pravila
Druga poruka: „Spremi ovo kao CLAUDE.md u mapu Reels i uvijek se drži ovih
pravila:” + sadržaj datoteke [`../CLAUDE.md`](../CLAUDE.md). Kopiraj i
`alati/provjeri_reel.py` u `Reels/alati/`.
