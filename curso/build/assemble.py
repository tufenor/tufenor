"""Junta os src/*.html na ordem, injeta barra de plantão, rodapé, numeração e índice.
Saída: dist/curso.html (a partir dele saem o PDF e o Word)."""
import os, re, html, math, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, DIST = ROOT / "src", ROOT / "dist"
# Livro a montar: por padrão o curso; BOOK_FILES escolhe outros arquivos (ex.: o dossiê avulso)
BOOK_FILES = os.environ.get("BOOK_FILES")
BOOK_HTML = os.environ.get("BOOK_HTML", "curso.html")
BOOK_TITLE = os.environ.get("BOOK_TITLE", "LULA GANHOU. PRA ONDE IR? · E-book patriota, contra a censura da esquerda · Patriota Anônimo")
SEC_RE = re.compile(r'<section class="page([^"]*)"([^>]*)>(.*?)</section>', re.S)
ATTR_RE = re.compile(r'data-([\w-]+)="([^"]*)"')
TOC_PER_PAGE = 21
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

def qr(m):
    """<!--QR:url--> vira um QR code em SVG inline."""
    import qrcode, qrcode.image.svg, io
    img = qrcode.make(m.group(1), image_factory=qrcode.image.svg.SvgPathImage, border=1)
    buf = io.BytesIO(); img.save(buf)
    s = buf.getvalue().decode("utf-8")
    return s[s.index("<svg"):]

def svg(m):
    return (SRC / "svg" / f"{m.group(1)}.svg").read_text(encoding="utf-8")

def load_pages():
    pages = []
    files = [SRC / f for f in BOOK_FILES.split(",")] if BOOK_FILES else sorted(SRC.glob("[0-9][0-9]-*.html"))
    for f in files:
        text = re.sub(r"<!--SVG:([\w-]+)-->", svg, f.read_text(encoding="utf-8"))
        text = re.sub(r"<!--QR:(\S+?)-->", qr, text)
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
        res.append({"cls": "nofill", "attrs": {"sec": "Índice", "part": "Pré-textual"}, "inner": f'{title}<ul class="toc">{items}</ul>'})
    return res

SRC_RE = re.compile(r'\s*<small class="src">(.*?)</small>', re.S)
FONTES_CHARS = 2300  # caracteres de fonte por página do anexo

def pull_sources(pages):
    """Tira a linha de fonte das páginas e guarda para o anexo."""
    for p in pages:
        found = SRC_RE.findall(p["inner"])
        p["inner"] = SRC_RE.sub("", p["inner"])
        p["srcs"] = [re.sub(r'<span class="pending">.*?</span>', "", f).strip() for f in found]
        p["srcs"] = [f for f in p["srcs"] if f]

def fontes_pages(pages):
    items, k = [p for p in pages if p.get("srcs")], 0
    chunks, cur, size = [], [], 0
    for p in items:
        n = sum(len(re.sub("<.*?>", "", s)) for s in p["srcs"]) + 40
        if cur and size + n > FONTES_CHARS:
            chunks.append(cur); cur, size = [], 0
        cur.append(p); size += n
    if cur:
        chunks.append(cur)
    res = []
    for i, ch in enumerate(chunks):
        attrs = {"sec": "Fontes", "part": "Anexos"}
        if i == 0:
            attrs.update({"toc": "Anexo · Fontes de todos os números", "toc-level": "part"})
        res.append({"cls": "nofill", "attrs": attrs, "inner": None, "chunk": ch, "first": i == 0})
    return res

def render_fontes(fp):
    head = ('<span class="kicker black">Anexo</span><h2>Fontes de todos os números</h2>'
            '<p style="font-size:8pt">Cada número do curso tem origem. Aqui estão, página por página.</p>') if fp["first"] else ""
    lis = "".join(f'<li><b>p. {p["num"]}</b>{" ".join(p["srcs"])}</li>' for p in fp["chunk"])
    return f'{head}<ul class="fontes">{lis}</ul>'

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
    idx = next((i for i, p in enumerate(pages) if "toc-here" in p["attrs"]), None)
    pull_sources(pages)
    if idx is None:  # livro sem índice (ex.: dossiê avulso)
        allp, n_toc = pages + fontes_pages(pages), 0
    else:
        before, after = pages[:idx + 1], pages[idx + 1:]
        after = after + fontes_pages(pages)
        # dois passes: primeiro descobrimos quantas páginas o índice ocupa
        n_toc = len(toc_pages(toc_entries(after, 0)))
        entries = toc_entries(after, len(before) + n_toc)
        allp = before + toc_pages(entries) + after
    for i, p in enumerate(allp):
        p["num"] = i + 1
    for p in allp:
        if p.get("chunk") is not None:
            p["inner"] = render_fontes(p)
    body = "\n".join(frame(p, i + 1) for i, p in enumerate(allp))
    DIST.mkdir(exist_ok=True)
    (DIST / BOOK_HTML).write_text(
        f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{html.escape(BOOK_TITLE)}</title><meta name="author" content="Patriota Anônimo">'
        f'<link rel="stylesheet" href="../style.css"></head><body>{body}</body></html>', encoding="utf-8")
    print(f"{len(allp)} páginas montadas ({n_toc} de índice)")

if __name__ == "__main__":
    main()
