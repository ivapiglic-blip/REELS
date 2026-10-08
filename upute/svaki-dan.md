# Svaki dan

## Primjer narudžbe
```text
U "1 Snimke" je video "Rovinj dron.mp4". Napravi 6 reelova od 30 s, svaki
s drugom temom:
1. Staro mjesto  2. More i brodovi  3. Plaže  4. Skrivena mjesta
5. Zalazak sunca  6. Najbolje od svega.
Za svaki napravi novu glazbu u ElevenLabsu prema temi. Na sve stavi
grafiku iz "3 Grafika/Moj logo" s natpisom ROVINJ.
Drži se pravila iz CLAUDE.md, pa mi pokaži pregled kadrova prije nego
spremiš u "4 Gotovo".
```

## Kad ti nešto ne paše
| Napišeš | Claude napravi |
|---|---|
| „Glazba je preslatka, treba jače” | Novu glazbu s tvrđim žanrom i dubljim basom, rezove ponovo poravna na novi ritam |
| „Ponavlja se isti kadar” | Strožu raspodjelu: kadar jednom, isto mjesto najviše 2 puta i razmaknuto |
| „Skrati na 15 s” | Kraće reelove, grafiku i jingle pomakne na novi kraj |
| „Logo je prevelik” | Promijeni veličinu u grafici i ponovo iscrta sloj |
| „Reel 3, kadar s crkvom van” | Zamijeni samo taj kadar i ponovo složi samo taj reel |

## Brza pomoć
- **Claude traži naredbu u Terminalu:** kopiraj točno, zalijepi, Enter. Lozinka samo tamo.
- **Reel kraći / slika završi prije glazbe:** „provjeri trajanje slike i zvuka”.
- **Grafika prekriva video sivom bojom:** „grafika nije prozirna, popravi render”.
- **Facebook stavlja „AI sadržaj”:** „skini metapodatke s gotovih reelova”.
- **Disk se puni:** „obriši radne datoteke starih reelova iz Cachesa, originale i gotove ne diraj”.

## Hetzner — samo za velike poslove
Za reelove ne treba. Za sate 4K rendera ili desetke videa odjednom:
1. Otvori račun na hetzner.com/cloud i dodaj karticu — **sama** (Claude ne upisuje podatke kartice).
2. U konzoli napravi API token i spremi ga u Keychain kao „Hetzner API”.
3. „Ovaj posao napravi na Hetzneru. Digni server, odradi render, rezultat
   vrati u ‘4 Gotovo’ i obavezno obriši server na kraju.”

Ugašen, a neobrisan server i dalje se plaća.
