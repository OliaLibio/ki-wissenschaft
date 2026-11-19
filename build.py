#!/usr/bin/env python3
"""Sammelt alle Beiträge aus posts/*.json, prüft sie und schreibt data/posts.json und feed.xml.
Aufruf: python3 build.py
"""
import glob, json, os, sys, html
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(ROOT, "posts")
OUT = os.path.join(ROOT, "data", "posts.json")
FEED = os.path.join(ROOT, "feed.xml")
SITE_URL = os.environ.get("SITE_URL", "https://olialibio.github.io/ki-wissenschaft/")

CATEGORIES = {"gesundheit", "tiere", "mythen", "klima", "archaeologie", "grenzen"}
MATURITY = {"lab", "study", "clinical", "deployed", "preprint", "review"}
EVIDENCE = {"meta", "rct", "cohort", "single", "animal", "review", "preprint"}
VERDICT = {"busted", "partly", "confirmed", "open"}
LANGS = ("de", "en", "ru")

def fail(msg):
    print("FEHLER:", msg, file=sys.stderr)
    sys.exit(1)

posts = []
seen = set()
for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.json"))):
    name = os.path.basename(path)[:-5]
    try:
        with open(path, encoding="utf-8") as f:
            p = json.load(f)
    except Exception as e:
        fail(f"{name}: kein gültiges JSON ({e})")
    if p.get("id") != name:
        fail(f"{name}: 'id' muss dem Dateinamen entsprechen")
    if name in seen:
        fail(f"{name}: doppelte id")
    seen.add(name)
    for key in ("date", "published", "category", "countries", "institution", "maturity", "source"):
        if key not in p:
            fail(f"{name}: Feld '{key}' fehlt")
    datetime.strptime(p["date"], "%Y-%m-%d")
    datetime.strptime(p["published"], "%Y-%m-%d")
    if p["category"] not in CATEGORIES:
        fail(f"{name}: unbekannte Rubrik {p['category']}")
    if p["maturity"] not in MATURITY:
        fail(f"{name}: unbekannter Reifegrad {p['maturity']}")
    if p["category"] == "mythen":
        if p.get("evidence") not in EVIDENCE or p.get("verdict") not in VERDICT:
            fail(f"{name}: Mythen-Beitrag braucht 'evidence' und 'verdict'")
    if not (p["source"].get("url", "").startswith("http") and p["source"].get("name")):
        fail(f"{name}: Quelle braucht 'name' und 'url'")
    for lang in LANGS:
        t = p.get(lang) or {}
        for key in ("title", "summary", "why", "caveat"):
            if not t.get(key):
                fail(f"{name}: {lang}.{key} fehlt")
        if p["category"] == "mythen" and not t.get("myth"):
            fail(f"{name}: {lang}.myth fehlt")
    im = p.get("image")
    if im is not None and not (isinstance(im, dict) and im.get("src","").startswith("http") and im.get("credit") and im.get("link","").startswith("http") and im.get("kind") in ("figure","press","photo")):
        fail(f"{name}: 'image' braucht src, credit, link (http…) und kind = figure|press|photo")
    if im is None:
        print(f"Hinweis: {name} hat kein Bild", file=sys.stderr)
    posts.append(p)

posts.sort(key=lambda p: (p["date"], p["id"]), reverse=True)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               "count": len(posts), "posts": posts}, f, ensure_ascii=False, indent=1)

# RSS-Feed (deutsch)
items = []
for p in posts[:60]:
    d = p["de"]
    link = f"{SITE_URL}#post/{p['id']}"
    desc = html.escape(f"{d['summary']}\n\nWarum das wichtig ist: {d['why']}\n\nVorbehalt: {d['caveat']}\n\nQuelle: {p['source']['name']} – {p['source']['url']}")
    pub = datetime.strptime(p["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 08:00:00 +0000")
    items.append(f"""  <item>
   <title>{html.escape(d['title'])}</title>
   <link>{link}</link>
   <guid isPermaLink="false">{p['id']}</guid>
   <pubDate>{pub}</pubDate>
   <category>{p['category']}</category>
   <description>{desc}</description>
  </item>""")
with open(FEED, "w", encoding="utf-8") as f:
    f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
 <channel>
  <title>KI in der Wissenschaft</title>
  <link>{SITE_URL}</link>
  <description>Montag, Mittwoch, Freitag: Was KI heute in der Forschung erreicht. Gesundheit, Tiere, Mythen-Check, Klima, Archäologie, Grenzen.</description>
  <language>de</language>
{chr(10).join(items)}
 </channel>
</rss>
""")
print(f"{len(posts)} Beiträge → data/posts.json, feed.xml")
