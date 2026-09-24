import json
from pathlib import Path

content = Path("content")

files = [
    "homepage.json",
    "historie.json",
    "souteze.json",
    "akce.json",
    "clenove.json",
    "vedeni.json"
]

for file in files:
    path = content / file

    with open(path, encoding="utf-8") as f:
        json.load(f)

print("Validace OK")
