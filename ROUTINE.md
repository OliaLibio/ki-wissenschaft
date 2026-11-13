# Arbeitsauftrag für den Mo/Mi/Fr-Agenten

Du pflegst die Webseite „KI in der Wissenschaft“ in diesem Repository. Deine Aufgabe heute: recherchiere neue, belegte Ergebnisse darüber, was Künstliche Intelligenz aktuell in der Forschung erreicht, und lege sie als Beiträge an. Lies zuerst README.md und zwei vorhandene Dateien in `posts/` als Muster.

## Recherche

- Suche weltweit, nicht nur im deutschsprachigen Raum. Schwerpunkte: USA, China, Großbritannien, Deutschland, Schweiz, Japan, Südkorea, Israel, Kanada, Frankreich.
- Bevorzugte Quellen: Nature, Science, The Lancet, NEJM, Cell, PNAS, JAMA, BMJ und ihre Schwesterjournale; Pressestellen von Universitäten und Instituten (EurekAlert, Phys.org, ScienceDaily, MIT News, Max-Planck, DeepMind, Earth Species Project, Project CETI, Vesuvius Challenge); arXiv und bioRxiv für Vorabdrucke.
- Nur Ergebnisse, die in den letzten 14 Tagen veröffentlicht oder bekannt geworden sind und noch nicht in `posts/` vorkommen. Prüfe die vorhandenen Dateinamen und Titel.
- Lies die Originalquelle oder die offizielle Pressemitteilung, nicht nur Blogs oder Aggregatoren. Übernimm Zahlen nur, wenn sie dort stehen.
- Meide Werbetexte von Herstellern ohne begutachtete Studie.

## Umfang pro Tag

- Vier bis sechs neue Beiträge, verteilt über mindestens drei der sechs Rubriken: `gesundheit`, `tiere`, `mythen`, `klima`, `archaeologie`, `grenzen`.
- Die Rubrik `grenzen` (Fehlschläge, Rückzüge, Grenzen der KI) mindestens einmal pro Woche bedienen.
- Die Rubrik `mythen` braucht ein `myth`-Feld (die geprüfte Behauptung), `evidence` und `verdict`. Hier zählt die Beweislage, nicht die Schlagzeile. Ein KI-Bezug ist willkommen, aber nicht Pflicht.

## Schreibstil

- Jeder Beitrag in allen drei Sprachen: `de`, `en`, `ru`. Deutsch ist die Leitsprache, Englisch und Russisch sind vollwertige Übersetzungen, keine Kurzfassungen.
- `title`: konkret, mit dem Ergebnis, ohne Clickbait.
- `summary`: vier bis sechs Sätze mit den wichtigsten Zahlen (Teilnehmer, Trefferquoten, Vergleichsgruppen), Institution und Methode.
- `why`: zwei Sätze, warum das für Laien relevant ist.
- `caveat`: ehrlich. Studiengröße, Vorabdruck ohne Begutachtung, Interessenkonflikte, fehlende Replikation.
- Keine Übertreibungen wie „Durchbruch“ oder „Revolution“, außer in Zitaten.

## Technisch

1. Neue Datei je Beitrag: `posts/JJJJ-MM-TT-kurzname.json`. `date` ist das heutige Datum, `published` das Datum der Quelle, `id` gleich dem Dateinamen ohne `.json`.
2. `python3 build.py` ausführen. Bei einem Fehler die Datei korrigieren, bis das Skript durchläuft.
3. Alle Änderungen committen (Nachricht: `Beiträge vom JJJJ-MM-TT: <Kurzliste der Titel>`) und auf `main` pushen.
4. Am Ende kurz berichten: welche Beiträge angelegt wurden, mit Quelle, und was du geprüft, aber verworfen hast und warum.

Wenn du an einem Tag weniger als drei belastbare neue Ergebnisse findest, veröffentliche lieber weniger als schwache Beiträge, und sage das im Bericht.
