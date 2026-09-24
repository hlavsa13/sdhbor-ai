import json
from pathlib import Path

CONTENT = Path("content")
GENERATED = Path("generated")

GENERATED.mkdir(exist_ok=True)

with open(CONTENT / "homepage.json", encoding="utf-8") as f:
    homepage = json.load(f)

html = f"""
<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="utf-8">
<title>{homepage['nazev']}</title>
</head>
<body>

<h1>{homepage['nazev']}</h1>

<p>{homepage['obec']}</p>

<p>Založeno: {homepage['rok_zalozeni']}</p>

<p>Počet členů: {homepage['pocet_clenu']}</p>

<p>{homepage['uvodni_text']}</p>

</body>
</html>
"""

with open(GENERATED / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html vytvořen")
