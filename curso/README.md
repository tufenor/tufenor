# LULA GANHOU. PRA ONDE IR? — curso (e-book A5)

Autor: **Patriota Anônimo**. E-book patriota, contra a censura da esquerda.

Build: `npm install && npm run build` (curso) · `npm run build:dossie` (dossiê avulso) · `npm run build:all` (os dois)

- `src/*.html`: páginas (`<section class="page" data-sec data-part data-toc>`). `<!--SVG:nome-->` injeta `src/svg/nome.svg`.
- `build/gen_svg.py`: ilustrações próprias (multidão verde-amarela, bandeira, mapa, “proibido comunismo”).
- `build/assemble.py`: barra de plantão, rodapé, numeração e índice → `dist/curso.html`.
- `build/fill.js`: preenche o espaço livre no pé das páginas com chamadas de tabloide.
- `build/check.js`: falha se algum conteúdo chegar a menos de 4 mm do rodapé.
- `build/render.js`: PDF A5. `build/todocx.py`: Word via pandoc.

Status: e-book completo (241 páginas): pré-textual, Partes 1 a 8, Bônus B1 a B7, anexos e fontes. Dossiê avulso (13 páginas). Kit de vendas em `vendas/` (página de vendas + roteiros, DM e e-mails). `npm run build:all` gera tudo em `dist/`.
