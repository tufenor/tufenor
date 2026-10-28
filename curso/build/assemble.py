"""Junta os src/*.html na ordem, injeta barra de plantão, rodapé, numeração e índice.
Saída: dist/curso.html (a partir dele saem o PDF e o Word)."""
import re, html, math, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, DIST = ROOT / "src", ROOT / "dist"
SEC_RE = re.compile(r'<section class="page([^"]*)"([^>]*)>(.*?)</section>', re.S)
ATTR_RE = re.compile(r'data-([\w-]+)="([^"]*)"')
TOC_PER_PAGE = 26
# letreiro de TV no rodapé: só fatos com fonte no corpo do curso
TICKER = [
    "IOF de 3,5% nas remessas, no cartão e no dinheiro vivo",
    "Dívida pública passa de R$ 11 trilhões",
    "Arrecadação federal recorde: R$ 2,9 trilhões em 2025",
    "43 medidas aumentaram a carga até mar/2026",
    "Bolívia: dólar oficial vai de Bs 6,96 para Bs 12,02",
    "Até R$ 450 bilhões de ajuste fiscal a partir de 2027",
    "Bolívia elege a centro-direita e encerra 20 anos de MAS",
    "USDT x remessa: até 6% a mais no seu bolso",
]

def svg(m):
    return (SRC / "svg" / f"{m.group(1)}.svg").read_text(encoding="utf-8")

def load_pages():
    pages = []
    for f in sorted(SRC.glob("[0-9][0-9]-*.html")):
        text = re.sub(r"<!--SVG:([\w-]+)-->", svg, f.read_text(encoding="utf-8"))
        for cls, attrs, inner in SEC_RE.findall(text):
            pages.append({"cls": cls.strip(), "attrs": dict(ATTR_RE.findall(attrs)), "inner": inner})
    return pages

def toc_entries(pages, offset):
    out = []
    for i, p in enumerate(pages):
        a = p["attrs"]
        if "toc" in a:
            out.append((a.get("toc-level", "chap"), a["toc"], i + 1 + offset))
    return out

def toc_pages(entries):
    n = max(1, math.ceil(len(entries) / TOC_PER_PAGE))
    res = []
    for k in range(n):
        items = "".join(
            f'<li class="{lvl}"><span>{html.escape(t)}</span><span class="d"></span><span class="pg">{pg}</span></li>'
            for lvl, t, pg in entries[k * TOC_PER_PAGE:(k + 1) * TOC_PER_PAGE])
        title = '<span class="kicker black">Índice</span><h1>O que tem aqui dentro</h1>' if k == 0 else ""
        res.append({"cls": "", "attrs": {"sec": "Índice", "part": "Pré-textual"}, "inner": f'{title}<ul class="toc">{items}</ul>'})
    return res

def frame(p, num):
    a, full = p["attrs"], "full" in p["cls"].split()
    bar = "" if full else (f'<div class="topbar"><span><span class="live">Plantão</span>{html.escape(a.get("part", ""))}</span>'
                           f'<span class="sec">{html.escape(a.get("sec", ""))}</span></div>')
    foot = "" if full else (f'<div class="footer"><span class="tick"><span class="flagdot"></span><b>ÚLTIMAS</b>{TICKER[num % len(TICKER)]}</span>'
                            f'<span class="num">{num}</span></div>')
    return f'<section class="page {p["cls"]}" data-num="{num}">{bar}<div class="content">{p["inner"]}</div>{foot}</section>'

def main():
    pages = load_pages()
    # o índice entra logo depois do marcador data-toc-here
    idx = next(i for i, p in enumerate(pages) if "toc-here" in p["attrs"])
    before, after = pages[:idx + 1], pages[idx + 1:]
    # dois passes: primeiro descobrimos quantas páginas o índice ocupa
    n_toc = len(toc_pages(toc_entries(after, 0)))
    entries = toc_entries(after, len(before) + n_toc)
    allp = before + toc_pages(entries) + after
    body = "\n".join(frame(p, i + 1) for i, p in enumerate(allp))
    DIST.mkdir(exist_ok=True)
    (DIST / "curso.html").write_text(
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>LULA GANHOU. PRA ONDE IR?</title>'
        f'<link rel="stylesheet" href="../style.css"></head><body>{body}</body></html>', encoding="utf-8")
    print(f"{len(allp)} páginas montadas ({n_toc} de índice)")

if __name__ == "__main__":
    main()
