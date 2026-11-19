# KI in der Wissenschaft

Eine statische Webseite, die montags, mittwochs und freitags je drei bis fünf neue Beiträge pro Rubrik darüber erhält, was Künstliche Intelligenz aktuell in der Forschung erreicht. Dreisprachig: Deutsch, Englisch, Russisch.

**Rubriken:** Gesundheit · Tiere · Mythen-Check · Klima & Umwelt · Archäologie & Geschichte · Grenzen & Fehlschläge

## Aufbau

| Pfad | Zweck |
|---|---|
| `posts/*.json` | Ein Beitrag pro Datei, alle drei Sprachen enthalten. Dateiname = `id` = `JJJJ-MM-TT-kurzname`. |
| `build.py` | Prüft alle Beiträge und erzeugt `data/posts.json` und `feed.xml`. |
| `index.html` | Die komplette Seite (HTML, CSS, JS in einer Datei), lädt `data/posts.json`. |
| `ROUTINE.md` | Der Arbeitsauftrag für den automatischen Mo/Mi/Fr-Agenten. |

## Neuen Beitrag anlegen

1. Datei `posts/JJJJ-MM-TT-kurzname.json` nach dem Muster der vorhandenen Beiträge anlegen.
2. `python3 build.py` ausführen. Das Skript bricht mit einer klaren Fehlermeldung ab, wenn ein Feld fehlt.
3. Commit und Push. GitHub Pages veröffentlicht automatisch.

### Felder

| Feld | Werte |
|---|---|
| `category` | `gesundheit`, `tiere`, `mythen`, `klima`, `archaeologie`, `grenzen` |
| `maturity` | `lab` (Labor), `study` (Studie), `clinical` (klinische Studie), `deployed` (im Einsatz), `preprint` (Vorabdruck), `review` (Übersicht) |
| `countries` | ISO-Ländercodes, z. B. `US`, `DE`, `CN`, oder `INT` für international |
| `evidence` | nur Mythen: `meta`, `rct`, `cohort`, `single`, `animal`, `review`, `preprint` |
| `verdict` | nur Mythen: `busted`, `partly`, `confirmed`, `open` |
| `published` | Datum, an dem die Forschung veröffentlicht wurde (Journal, Vorabdruck oder Pressemitteilung), nicht das Anlagedatum |
| `image` | `{"src": URL, "kind": "figure"\|"press"\|"photo", "credit": Bildnachweis, "link": Seite des Bildes}` |
| `de` / `en` / `ru` | je `title`, `summary`, `why`, `caveat`, bei Mythen zusätzlich `myth` |

## Lokal ansehen

```bash
python3 -m http.server 8765
```

Dann http://localhost:8765 öffnen. Die Seite braucht einen Webserver, weil sie `data/posts.json` per `fetch` lädt.
