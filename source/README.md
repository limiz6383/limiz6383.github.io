# Portfolio source

`index.html` in the repo root is generated. This folder holds what it is built from, so every change shows up as a readable commit.

- `src_v1_backup.html`: the page template, with the copy, structure and script
- `build_v3.py`: restyles it (fonts, type scale, layout rules) and writes `src_v3.html`
- `assemble3.py`: inlines the images and the resume PDF into one self-contained `index.html`
- `img/`: portrait art and project screenshots

Fonts are Newsreader, Hanken Grotesk and Caveat, embedded from `@fontsource`. The scripts still use the paths from the machine they were written on, so change the paths at the top of each script before running them. The resume PDF is not included here; it is embedded in the built page.

AI answers on the live site go through a small proxy in `proxy/`, which holds the API key. The key never appears in the page.
