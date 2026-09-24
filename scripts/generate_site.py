import json
from pathlib import Path

content = Path("content")
generated = Path("generated")

generated.mkdir(exist_ok=True)

with open(content / "homepage.json", encoding="utf-8") as f:
    homepage = json.load(f)

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{homepage["nazev"]}</title>
</head>
<body>
<h1>{homepage["nazev"]}</h1>
<p>{homepage["obec"]}</p>
</body>
</html>
"""

with open(generated / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Web vygenerován")
