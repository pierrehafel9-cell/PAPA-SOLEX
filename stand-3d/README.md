# Stand Flora & Co — maquette 3D

Modélisateur 3D du stand de sacs (6 m², 1,50 m de haut max) placé devant la vitrine
Paul & Anna de la galerie, avec le passage chariots obligatoire entre la vitrine et le stand.

- `index.html` : la maquette, à ouvrir directement dans un navigateur (photos intégrées).
- `src/app.html` : le code source (photos remplacées par des marqueurs `%%…%%`).
- `assets/` : photos du lieu (façade, caisses Carrefour, photos de référence).
- `build.py` : régénère `index.html` et `dist/artifact.html` après une modification de `src/app.html`.

```
python3 build.py
```
