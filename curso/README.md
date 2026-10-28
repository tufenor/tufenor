# LULA GANHOU. PRA ONDE IR? — curso (e-book A5)

Autor: **Patriota Anônimo**. E-book patriota, contra a censura da esquerda.

Build: `npm install && npm run build`

- `src/*.html`: páginas (`<section class="page" data-sec data-part data-toc>`). `<!--SVG:nome-->` injeta `src/svg/nome.svg`.
- `build/gen_svg.py`: ilustrações próprias (multidão verde-amarela, bandeira, mapa, “proibido comunismo”).
- `build/assemble.py`: barra de plantão, rodapé, numeração e índice → `dist/curso.html`.
- `build/fill.js`: preenche o espaço livre no pé das páginas com chamadas de tabloide.
- `build/check.js`: falha se algum conteúdo chegar a menos de 4 mm do rodapé.
- `build/render.js`: PDF A5. `build/todocx.py`: Word via pandoc.

Status: Pré-textual + Partes 1 a 5 prontas (163 páginas). Próximas: Partes 6 a 8, Bônus e Anexos.
