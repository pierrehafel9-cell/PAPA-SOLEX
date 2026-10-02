#!/usr/bin/env python3
"""Assemble la maquette : intègre les photos (data URI) dans src/app.html.

Produit :
  - dist/artifact.html : corps de page (sans <html>/<head>), pour la publication en Artifact
  - index.html         : page autonome à ouvrir dans un navigateur
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
ASSETS = ROOT / "assets"


def data_uri(name: str) -> str:
    raw = (ASSETS / name).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(raw).decode("ascii")


def main() -> None:
    src = (ROOT / "src" / "app.html").read_text(encoding="utf-8")
    repl = {"%%FACADE%%": data_uri("facade.jpg"), "%%CARREFOUR%%": data_uri("carrefour.jpg")}
    for i in range(1, 6):
        repl[f"%%PHOTO{i}%%"] = data_uri(f"photo{i}.jpg")
    for k, v in repl.items():
        if k not in src:
            raise SystemExit(f"placeholder manquant : {k}")
        src = src.replace(k, v)

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "artifact.html").write_text(src, encoding="utf-8")

    standalone = (
        '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n"
        + src
        + "\n</body>\n</html>\n"
    )
    (ROOT / "index.html").write_text(standalone, encoding="utf-8")
    print(f"ok : {len(src) / 1024:.0f} Ko")


if __name__ == "__main__":
    main()
