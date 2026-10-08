# Ivini reelovi — pravila

Claude ovu datoteku čita na početku svakog rada. Pravila su naučena na stvarnim
reelovima (Mirkovo iskustvo), uključujući greške koje su se već jednom dogodile.

## Kako radimo
- Piši mi na hrvatskom, kratko i jasno. Ja nisam programerka.
- Ne govori "gotovo" dok sam ne provjeriš rezultat (pogledaj kadrove,
  trajanje, zvuk).
- Nikad ne briši ni ne mijenjaj originalne snimke u "1 Snimke". Radne
  datoteke drži u ~/Library/Caches/reels, gotove reelove spremaj u "4 Gotovo".
- Ništa ne objavljuj na društvene mreže i ne šalji nikome bez mog
  izričitog "objavi" ili "šalji".
- Ključeve (ElevenLabs, Hetzner i ostale) drži samo u macOS Keychainu, nikad
  kao tekst u datotekama ili razgovoru. Čitaj ih s
  `security find-generic-password -s "ElevenLabs API" -w`.
- Velike datoteke ne stavljaj na Desktop ni u iCloud mape.
- Prije spremanja u "4 Gotovo" pokaži mi pregled kadrova (contact sheet).

## Izlazni format
- 1080×1920 (9:16), H.264 High, CRF 17–18, 25 ili 30 fps (isto kao
  snimka), AAC 256 kb/s, 48 kHz, -movflags +faststart.
- Glasnoća oko −12 LUFS (integrated).
- Trajanje TOČNO kako tražim (zadano 30 s). Provjeri da slika i zvuk
  traju jednako dugo, inače slika završi prije glazbe.
- Nakon rendera pokreni `python3 alati/provjeri_reel.py <reel.mp4>` i
  popravi sve što javi kao GREŠKA.

## Kadrovi i rezovi
- Svaki kadar u jednom reelu samo jednom. Isto mjesto najviše 2 puta i
  razmaknuto (ne jedno za drugim).
- Rezove poravnaj na ritam glazbe (udarci / taktovi). Kad se glazba
  promijeni, ponovo poravnaj rezove na novi ritam.
- Svaki reel ima svoju temu; ne dijeli iste kadrove među reelovima iste
  serije ako se može izbjeći.

## Glazba (ElevenLabs)
- Za reel od 30 s generiraj ~36 s glazbe i uzmi KRAJ pjesme (zadnjih 30 s),
  jer je kraj najljepši i čisto završava na zadnjem taktu.
- Opis: žanr + tempo (120–128 BPM) + raspoloženje + jedan glavni instrument.
  Uvijek dodaj na kraj opisa dodatak iz `upute/glazba.md`.
- Nikad "veselo/ljetno" s marimbom, ukulelom ili zviždanjem — zvuči dječje.
- Zvuk jinglea (Sound Effects) stavi točno na trenutak kad logo udari.

## Grafika od dizajnera
- Paketi su u "3 Grafika/<naziv>". Pročitaj upute iz paketa i iscrtaj sloj
  kao ProRes 4444 s alfa kanalom.
- PROVJERI da je pozadina stvarno prozirna (alfa kanal postoji i nije
  posvuda 255). Neprozirna pozadina prekrije cijeli video sivom/crnom.
- PROVJERI da na slici nema trake playera / kontrola preglednika na dnu
  (puppeteer mora renderirati čisti kadar, bez UI-ja).
- Logo i naslov stoje oko 60 % visine kadra, da ne smetaju tekstu i
  gumbima Instagrama.
- Kad se reel skrati/produži, pomakni grafiku i jingle na novi kraj.

## Metapodaci
- S gotovih reelova skini metapodatke (`-map_metadata -1`, bez C2PA /
  "AI" oznaka), inače Facebook stavlja oznaku „AI sadržaj”.

## Server (Hetzner) — samo za velike poslove
- Samo kad izričito kažem. Token iz Keychaina ("Hetzner API").
- Podatke kartice nikad ne upisuješ ti.
- Na kraju OBAVEZNO obriši server (ugašen, a neobrisan server se i dalje plaća)
  i javi mi da je obrisan.
