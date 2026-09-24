import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

CONTENT = Path("content")
GENERATED = Path("generated")
TEMPLATES = Path("templates")

GENERATED.mkdir(exist_ok=True)

# načtení dat
with open(CONTENT / "homepage.json", encoding="utf-8") as f:
    homepage = json.load(f)

# načtení šablony
env = Environment(
    loader=FileSystemLoader(TEMPLATES),
    autoescape=False
)

template = env.get_template("index.j2")

# render
html = template.render(**homepage)

# uložení
with open(GENERATED / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html vytvořen")
