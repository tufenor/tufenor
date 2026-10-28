# LULA GANHOU. PRA ONDE IR? — curso (e-book A5)

Build: `npm install && npm run build`

- `src/*.html`: páginas (`<section class="page" data-sec data-part data-toc>`). `<!--SVG:nome-->` injeta `src/svg/nome.svg`.
- `build/gen_svg.py`: ilustrações próprias (multidão verde-amarela, bandeira, mapa, “proibido comunismo”).
- `build/assemble.py`: barra de plantão, rodapé, numeração e índice → `dist/curso.html`.
- `build/check.js`: falha se algum conteúdo chegar a menos de 4 mm do rodapé.
- `build/render.js`: PDF A5. `build/todocx.py`: Word via pandoc.

Status: Pré-textual + Parte 1 prontas (24 páginas). Próximas: Partes 2 a 8, Bônus e Anexos.
