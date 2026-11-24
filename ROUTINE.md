# Arbeitsauftrag für den Mo/Mi/Fr-Agenten

Du pflegst die Webseite „KI in der Wissenschaft“ in diesem Repository. Deine Aufgabe heute: recherchiere neue, belegte Ergebnisse darüber, was Künstliche Intelligenz aktuell in der Forschung erreicht, und lege sie als Beiträge an. Lies zuerst README.md und zwei vorhandene Dateien in `posts/` als Muster.

## Recherche

- Suche weltweit, nicht nur im deutschsprachigen Raum. Schwerpunkte: USA, China, Großbritannien, Deutschland, Schweiz, Japan, Südkorea, Israel, Kanada, Frankreich.
- Bevorzugte Quellen: Nature, Science, The Lancet, NEJM, Cell, PNAS, JAMA, BMJ und ihre Schwesterjournale; Pressestellen von Universitäten und Instituten (EurekAlert, Phys.org, ScienceDaily, MIT News, Max-Planck, DeepMind, Earth Species Project, Project CETI, Vesuvius Challenge); arXiv und bioRxiv für Vorabdrucke.
- **Zeitraum, in dieser Reihenfolge:**
  1. Zuerst Ergebnisse, die in den letzten 14 Tagen veröffentlicht wurden.
  2. Reicht das nicht für drei Beiträge in einer Rubrik, suche Ergebnisse aus den letzten 3 Monaten.
  3. Reicht auch das nicht, suche bis 6 Monate zurück. Ältere Ergebnisse nur, wenn sie für das Verständnis eines aktuellen Beitrags unverzichtbar sind.
- Prüfe vorhandene Dateinamen und Titel in `posts/`. Kein Thema doppelt, auch nicht mit anderer Quelle.
- Lies die Originalquelle oder die offizielle Pressemitteilung, nicht nur Blogs oder Aggregatoren. Übernimm Zahlen nur, wenn sie dort stehen.
- Meide Werbetexte von Herstellern ohne begutachtete Studie.

## Umfang pro Lauf

- **Pro Rubrik mindestens drei, höchstens fünf neue Beiträge.** Es gibt sechs Rubriken: `gesundheit`, `tiere`, `mythen`, `klima`, `archaeologie`, `grenzen`. Ein Lauf ergibt also mindestens 18 und höchstens 30 neue Beiträge.
- Drei pro Rubrik sind der Normalfall. Einen vierten oder fünften Beitrag nur, wenn das Ergebnis wirklich bemerkenswert ist.
- Weniger als drei in einer Rubrik ist nicht akzeptabel. Wenn die letzten 14 Tage zu wenig hergeben, greife wie oben beschrieben auf die letzten 3 bis 6 Monate zurück.
- Die Rubrik `mythen` braucht ein `myth`-Feld (die geprüfte Behauptung), `evidence` und `verdict`. Hier zählt die Beweislage, nicht die Schlagzeile. Ein KI-Bezug ist willkommen, aber nicht Pflicht: Gesundheits- und Ernährungsmythen, die eine aktuelle große Studie prüft, passen immer.
- Bei `archaeologie` zählt jede Forschung, in der KI, maschinelles Lernen oder automatisierte Bild- oder Textauswertung zu einem Ergebnis über Vergangenheit, alte Texte, Fundstätten oder Fossilien beigetragen hat.

## Arbeitsweise bei 18 und mehr Beiträgen

- Arbeite **Rubrik für Rubrik**: recherchieren, drei bis fünf Beiträge schreiben, `python3 build.py`, committen und pushen, dann die nächste Rubrik. So geht bei einem Abbruch nichts verloren.
- Commit-Nachricht pro Rubrik: `Beiträge vom JJJJ-MM-TT, <Rubrik>: <Kurzliste>`.
- Halte die Texte so knapp wie im Muster, damit der Lauf nicht zu lang wird.

## Veröffentlichungsdatum

- `published` ist **das Datum, an dem die Forschung veröffentlicht wurde**: Online-Erscheinungsdatum der Studie im Journal, des Vorabdrucks oder der offiziellen Pressemitteilung, in dieser Reihenfolge. Nicht das Datum, an dem du den Beitrag anlegst.
- Die Seite zeigt dieses Datum oben auf jedem Beitrag als „Forschung veröffentlicht am“. Es muss also stimmen. Wenn du es nicht sicher findest, nimm den Beitrag nicht auf.

## Bild

- Jeder Beitrag bekommt ein Feld `image` mit `src`, `kind`, `credit` und `link`, siehe README.md.
- Reihenfolge der Bildquellen:
  1. **Abbildung aus der Studie** (`kind: "figure"`). Bei Springer-Nature-Journalen (Nature, Nature Medicine, Nature Communications, Scientific Reports usw.) lautet die URL der ersten Abbildung: `https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2F<DOI-Suffix>/MediaObjects/<Journalnummer>_<Jahr>_<Artikelnummer>_Fig1_HTML.png`, Beispiel für DOI 10.1038/s41586-026-11167-2: `.../art%3A10.1038%2Fs41586-026-11167-2/MediaObjects/41586_2026_11167_Fig1_HTML.png`. credit: „Abbildung 1 der Studie, <Journal>“.
  2. **Bild der Pressemitteilung** (`kind: "press"`): das `og:image` der Seite (im HTML `<meta property="og:image" content="…">`). Keine Logos, keine Standardbilder des Portals. credit: „Bild: <Herausgeber>“.
  3. **Freies Foto von Wikimedia Commons** (`kind: "photo"`), Suche über `https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch=<Suchbegriff>%20filetype:bitmap&gsrnamespace=6&gsrlimit=5&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=960`. Nimm `thumburl` (ohne `?utm…`-Anhang), Autor aus `Artist`, Lizenz aus `LicenseShortName`. credit: „Foto: <Autor>, <Lizenz>, Wikimedia Commons“, link: die `descriptionurl`.
- Prüfe jede Bild-URL mit `curl -s -o /dev/null -w "%{http_code} %{content_type}" -A "Mozilla/5.0" <url>`. Nur `200` mit `image/...` ist gültig. Sonst die nächste Bildquelle nehmen.

## Wunschthemen

Diese Themen hat sich die Leserin gewünscht. Erledige sie im genannten Lauf **zuerst**, sie zählen zu den drei bis fünf Beiträgen ihrer Rubrik. Danach lösche die erledigte Zeile aus dieser Liste und committe das mit.

- **Lauf am 2026-11-25 (Mittwoch), Rubrik `mythen`:** ein Mythen-Check zu **Vitamin D**. Geeignete Behauptungen zum Beispiel: „Vitamin-D-Tabletten schützen vor Erkältungen / Knochenbrüchen / Krebs / Depression“ oder „Wer viel draußen ist, hat genug Vitamin D“. Am besten eine aktuelle große Studie oder Übersichtsarbeit. Gibt es in den letzten sechs Monaten keine, nimm die maßgebliche große Studie (zum Beispiel einen großen randomisierten Versuch oder eine Cochrane-Übersicht), auch wenn sie älter ist, und gib ihr echtes Veröffentlichungsdatum an.

## Schreibstil: einfache Sprache

Die Leserinnen und Leser sind neugierige Laien ohne naturwissenschaftliche Ausbildung. Jeder Beitrag muss beim ersten Lesen verständlich sein. Schreib so, wie man es einer interessierten Freundin am Küchentisch erklären würde.

**Regeln**

- **Kurze Sätze**, höchstens etwa 15 Wörter. Ein Gedanke pro Satz.
- **Keine Namen von Forschenden** im Text. Die Institution steht ohnehin im Feld `institution`; im Text höchstens „Forschende aus Kanada“ oder „ein Team einer US-Universität“.
- **Keine Fachwörter.** Wenn eines unvermeidlich ist, sofort in Alltagssprache erklären: „Bauchfett, also Fett, das zwischen den Organen sitzt“. Verboten ohne Erklärung sind zum Beispiel: metabolisches Syndrom, HbA1c, DXA, MRT, Kohorte, randomisiert, Placebo, Biomarker, Inzidenz, Metaanalyse, Algorithmus, neuronales Netz, Proteine, Enzyme, Sensitivität, Spezifität, Konfidenzintervall, signifikant.
- **Wenige, runde Zahlen.** Höchstens zwei oder drei pro Beitrag. „Fast 60.000 Menschen“ statt „59.269 Teilnehmer“; „etwa jeder Fünfte“ statt „20 Prozent (12.073)“.
- **Bilder aus dem Alltag** helfen: Vergleiche, Beispiele, „stell dir vor …“.
- **Keine Abkürzungen** außer allgemein bekannten (KI, USA, CO2).

**Felder**

- `title`: eine klare Aussage in Alltagssprache, höchstens etwa 12 Wörter. Was ist herausgekommen? Kein Fachbegriff.
- `summary` (**Worum geht es und was kam heraus**): drei bis fünf kurze Sätze. Erst die Frage, die die Forschenden hatten. Dann, was sie gemacht haben, in einem Satz. Dann das Ergebnis.
- `why` (auf der Seite „Was heißt das für mich?“): ein bis zwei Sätze, was die Leserin daraus für ihren Alltag oder ihr Weltbild mitnehmen kann.
- `caveat` (auf der Seite „Der Haken“): ein bis zwei Sätze, warum man das Ergebnis noch nicht überbewerten sollte, in Alltagssprache („Es waren nur 40 Menschen“, „Bisher nur an Mäusen getestet“, „Die Firma, die das Mittel verkauft, hat die Studie bezahlt“).
- `myth` (nur Mythen-Check): die Behauptung so, wie man sie im Alltag hört.
- Englisch und Russisch: genauso einfach, keine Fachsprache, vollwertige Übersetzungen.
- Keine Übertreibungen wie „Durchbruch“ oder „Revolution“.

**Beispiel, wie es NICHT sein soll:** „Ein Team um X und Y vom Z Research Center wertete Daten von 59.269 Teilnehmern der UK Biobank aus, bei denen Körperzusammensetzung per DXA und MRT gemessen worden war. Rund 20 Prozent erfüllten die Kriterien eines metabolischen Syndroms.“

**So ist es richtig:** „Viele glauben: Je mehr Muskeln, desto gesünder der Stoffwechsel. Forschende aus den USA haben das bei fast 60.000 Erwachsenen in Großbritannien überprüft. Sie haben genau gemessen, wie viel Muskeln und Fett jeder hat und wo das Fett sitzt. Ergebnis: Mehr Muskeln allein schützen nicht. Entscheidend ist vor allem das Fett im Bauch, das sich zwischen den Organen versteckt.“

## Technisch

1. Neue Datei je Beitrag: `posts/JJJJ-MM-TT-kurzname.json`. `date` ist das heutige Datum, `published` das Datum der Quelle, `id` gleich dem Dateinamen ohne `.json`.
2. `python3 build.py` ausführen. Bei einem Fehler die Datei korrigieren, bis das Skript durchläuft.
3. Alle Änderungen committen (Nachricht: `Beiträge vom JJJJ-MM-TT: <Kurzliste der Titel>`) und auf `main` pushen.
4. Prüfe nach dem Push mit `git ls-remote origin main`, dass der Commit wirklich auf GitHub angekommen ist. Wenn nicht, sag das im Bericht deutlich.
5. Am Ende kurz berichten: welche Beiträge angelegt wurden, mit Quelle, und was du geprüft, aber verworfen hast und warum.

Qualität vor Aktualität: Lieber ein belastbares Ergebnis von vor vier Monaten als eine schwache Meldung von gestern. Ziel sind immer drei bis fünf Beiträge pro Rubrik, notfalls aus den letzten sechs Monaten.
