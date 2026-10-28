"""Gera as ilustrações próprias (sem pessoas reais) usadas no curso: src/svg/*.svg"""
import random, math, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "src" / "svg"
G, Y, B, W, K, R = "#009C3B", "#FFDF00", "#002776", "#fff", "#000", "#D7191C"

def flag(x, y, w, wave=0):
    h = w * 0.7
    d = f"M{x},{y} q{w/4},{-wave} {w/2},0 t{w/2},0 v{h} q{-w/4},{wave} {-w/2},0 t{-w/2},0 z"
    cx, cy = x + w / 2, y + h / 2
    return (f'<path d="{d}" fill="{G}"/>'
            f'<polygon points="{cx},{y+h*0.1} {x+w*0.92},{cy} {cx},{y+h*0.9} {x+w*0.08},{cy}" fill="{Y}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{h*0.22}" fill="{B}"/>'
            f'<path d="M{cx-h*0.22},{cy-h*0.03} q{h*0.22},{-h*0.08} {h*0.44},{h*0.05}" stroke="{W}" stroke-width="{h*0.04}" fill="none"/>')

def person(x, base, s, color, arm=None):
    head = f'<circle cx="{x}" cy="{base-38*s}" r="{7*s}" fill="{color}"/>'
    body = f'<path d="M{x-11*s},{base} v-{22*s} q0,-{8*s} {11*s},-{8*s} q{11*s},0 {11*s},{8*s} v{22*s} z" fill="{color}"/>'
    out = head + body
    if arm:  # braço erguido segurando mastro/placa
        out += f'<line x1="{x+8*s}" y1="{base-26*s}" x2="{x+14*s}" y2="{base-52*s}" stroke="{color}" stroke-width="{4*s}" stroke-linecap="round"/>'
    return out

def crowd(w=600, h=180, seed=7, bg=None, flags=9, signs=(), dark=False):
    random.seed(seed)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMax slice">']
    if bg: parts.append(f'<rect width="{w}" height="{h}" fill="{bg}"/>')
    rows = [(h - 70, 0.8, "#1d6b3a" if not dark else "#1a1a1a"), (h - 40, 1.0, "#0f4f29" if not dark else "#0d0d0d"), (h + 2, 1.25, "#062e17" if not dark else "#000")]
    poles = []
    for ri, (base, s, col) in enumerate(rows):
        x = random.uniform(-10, 10)
        while x < w + 20:
            arm = random.random() < 0.18
            shirt = random.choice([G, Y, Y, G, col]) if ri == 2 else col
            parts.append(person(x, base, s, shirt if ri == 2 else col, arm))
            if ri == 2 and shirt != col:  # cabeça na cor da multidão, camisa verde-amarela
                parts.append(f'<circle cx="{x}" cy="{base-38*s}" r="{7*s}" fill="{col}"/>')
            if arm: poles.append((x + 14 * s, base - 52 * s, s))
            x += random.uniform(17, 26) * s
    random.shuffle(poles)
    for i, (px, py, s) in enumerate(poles[:flags]):
        fw = 34 * s
        parts.insert(2, f'<line x1="{px}" y1="{py+10}" x2="{px}" y2="{py-26*s}" stroke="#333" stroke-width="2"/>' + flag(px, py - 26 * s, fw, wave=4))
    for i, (txt, sx) in enumerate(signs):
        sy = h - 150
        sw = len(txt) * 8 + 16
        parts.append(f'<g transform="rotate({random.choice([-4,-2,3,5])} {sx} {sy})"><line x1="{sx}" y1="{sy+20}" x2="{sx}" y2="{sy+70}" stroke="#333" stroke-width="3"/>'
                     f'<rect x="{sx-sw/2}" y="{sy-8}" width="{sw}" height="30" fill="{W}" stroke="{K}" stroke-width="2"/>'
                     f'<text x="{sx}" y="{sy+12}" font-family="Anton" font-size="13" text-anchor="middle" fill="{G}">{txt}</text></g>')
    parts.append("</svg>")
    return "".join(parts)

def big_flag(w=300):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {w*0.7}">{flag(0, 0, w)}</svg>'

def no_communism():
    # foice e martelo dentro de um sinal de proibido — ilustração própria
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'
            f'<circle cx="100" cy="100" r="92" fill="{W}" stroke="{R}" stroke-width="16"/>'
            f'<g fill="{K}">'
            f'<path d="M70,60 a52,52 0 1 0 74,58 l-14,-6 a38,38 0 1 1 -50,-44 z"/>'
            f'<rect x="88" y="62" width="14" height="88" rx="3" transform="rotate(40 95 106)"/>'
            f'<rect x="102" y="54" width="44" height="18" rx="3" transform="rotate(40 124 63)"/>'
            f'<path d="M60,148 l18,-6 l6,8 z"/></g>'
            f'<line x1="35" y1="35" x2="165" y2="165" stroke="{R}" stroke-width="16"/></svg>')

def route_map():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 170">'
            f'<rect width="400" height="170" fill="#EFEFEF"/>'
            f'<path d="M150,20 C230,10 330,40 360,90 C380,130 330,160 260,160 C220,160 200,140 180,120 C160,100 140,70 150,20 z" fill="{G}" opacity=".85"/>'
            f'<text x="290" y="105" font-family="Anton" font-size="22" fill="{Y}">BRASIL</text>'
            f'<path d="M40,60 C70,45 120,50 145,75 C150,100 135,130 100,138 C70,140 40,120 38,95 z" fill="#C8C8C8" stroke="{K}" stroke-width="2"/>'
            f'<text x="58" y="100" font-family="Anton" font-size="17" fill="{K}">BOLÍVIA</text>'
            f'<circle cx="300" cy="125" r="6" fill="{R}"/><text x="310" y="140" font-size="11" font-family="Archivo" font-weight="800">São Paulo</text>'
            f'<circle cx="95" cy="112" r="6" fill="{R}"/><text x="58" y="130" font-size="11" font-family="Archivo" font-weight="800">Santa Cruz</text>'
            f'<path d="M298,122 Q200,40 100,108" stroke="{K}" stroke-width="3" stroke-dasharray="8 6" fill="none"/>'
            f'<g transform="translate(196,58) rotate(-8)"><path d="M0,0 l22,4 l-22,4 l4,-4 z" fill="{K}"/></g>'
            f'<rect x="150" y="18" width="110" height="26" fill="{K}"/><text x="205" y="37" text-anchor="middle" font-family="Anton" font-size="15" fill="{Y}">≈ 3 H DE VOO</text>'
            f'</svg>')

def megaphone():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 90">'
            f'<path d="M15,35 h20 l55,-28 v76 l-55,-28 h-20 z" fill="{R}"/>'
            f'<rect x="20" y="55" width="12" height="25" fill="{K}"/>'
            f'<path d="M98,25 q12,20 0,40 M106,15 q20,30 0,60" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>')

files = {
    "crowd.svg": crowd(signs=[("BRASIL ACIMA DE TUDO", 140), ("LIBERDADE!", 460)]),
    "crowd-cover.svg": crowd(w=600, h=200, seed=3, flags=12, signs=[("MAIS 4 ANOS?", 470)], dark=True),
    "crowd-wide.svg": crowd(w=700, h=170, seed=11, flags=10, signs=[("DEUS, PÁTRIA, FAMÍLIA", 200), ("FORA COMUNISMO", 540)]),
    "flag.svg": big_flag(),
    "no-communism.svg": no_communism(),
    "route-map.svg": route_map(),
    "megaphone.svg": megaphone(),
}
for n, s in files.items():
    (OUT / n).write_text(s, encoding="utf-8")
print("ok", list(files))
