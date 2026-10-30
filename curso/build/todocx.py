"""HTML → Word via pandoc (remove SVG decorativo, barra, rodapé e chamadas de preenchimento)."""
import os, subprocess, pathlib
from bs4 import BeautifulSoup

DIST = pathlib.Path(__file__).resolve().parent.parent / "dist"
soup = BeautifulSoup((DIST / os.environ.get("BOOK_HTML", "curso.html")).read_text(encoding="utf-8"), "lxml")
for sel in ["svg", ".topbar", ".footer", ".filler", ".stamp", ".tape"]:
    for el in soup.select(sel):
        el.decompose()
# cada página vira uma seção separada por linha horizontal
for page in soup.select("section.page"):
    page.insert(0, soup.new_tag("hr"))
tmp = DIST / "_docx.html"
tmp.write_text(str(soup), encoding="utf-8")
subprocess.run(["pandoc", str(tmp), "-f", "html", "-t", "docx",
                "-o", str(DIST / (os.environ.get("BOOK_OUT", "LULA-GANHOU-Curso-Completo") + ".docx")), "--resource-path", str(DIST)], check=True)
tmp.unlink()
print("DOCX gerado")
