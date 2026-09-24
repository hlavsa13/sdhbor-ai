import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

CONTENT = Path("content")
GENERATED = Path("generated")
TEMPLATES = Path("templates")

GENERATED.mkdir(exist_ok=True)

env = Environment(
    loader=FileSystemLoader(TEMPLATES),
    autoescape=False
)

# Homepage
with open(CONTENT / "homepage.json", encoding="utf-8") as f:
    homepage = json.load(f)

template = env.get_template("index.j2")

with open(GENERATED / "index.html", "w", encoding="utf-8") as f:
    f.write(template.render(**homepage))

# Historie
with open(CONTENT / "historie.json", encoding="utf-8") as f:
    historie = json.load(f)

template = env.get_template("historie.j2")

with open(GENERATED / "historie.html", "w", encoding="utf-8") as f:
    f.write(template.render(historie=historie))

# Soutěže
with open(CONTENT / "souteze.json", encoding="utf-8") as f:
    souteze = json.load(f)

template = env.get_template("souteze.j2")

with open(GENERATED / "souteze.html", "w", encoding="utf-8") as f:
    f.write(template.render(souteze=souteze))

# Akce
with open(CONTENT / "akce.json", encoding="utf-8") as f:
    akce = json.load(f)

template = env.get_template("akce.j2")

with open(GENERATED / "akce.html", "w", encoding="utf-8") as f:
    f.write(template.render(**akce))

# Členové
with open(CONTENT / "clenove.json", encoding="utf-8") as f:
    clenove = json.load(f)

with open(CONTENT / "vedeni.json", encoding="utf-8") as f:
    vedeni = json.load(f)

template = env.get_template("clenove.j2")

with open(GENERATED / "clenove.html", "w", encoding="utf-8") as f:
    f.write(template.render(
        clenove=clenove,
        vedeni=vedeni
    ))

print("Všechny stránky vytvořeny")
