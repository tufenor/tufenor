"""HTML → Word via pandoc (remove SVG decorativo, barra e rodapé)."""
import re, subprocess, pathlib
DIST = pathlib.Path(__file__).resolve().parent.parent / "dist"
h = (DIST / "curso.html").read_text(encoding="utf-8")
h = re.sub(r"<svg.*?</svg>", "", h, flags=re.S)
h = re.sub(r'<div class="(topbar|footer)">.*?</div></div>|<div class="(topbar|footer)">.*?</span></div>', "", h, flags=re.S)
h = re.sub(r'<section class="page[^"]*"[^>]*>', '<section><hr/>', h)
tmp = DIST / "_docx.html"
tmp.write_text(h, encoding="utf-8")
subprocess.run(["pandoc", str(tmp), "-f", "html", "-t", "docx", "-o", str(DIST / "LULA-GANHOU-Curso-Completo.docx")], check=True)
tmp.unlink()
print("DOCX gerado")
