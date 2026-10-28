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

def house(x, y, s, color, roof):
    return (f'<polygon points="{x},{y+18*s} {x+20*s},{y} {x+40*s},{y+18*s}" fill="{roof}"/>'
            f'<rect x="{x+4*s}" y="{y+18*s}" width="{32*s}" height="{24*s}" fill="{color}"/>'
            f'<rect x="{x+16*s}" y="{y+28*s}" width="{8*s}" height="{14*s}" fill="{W}"/>'
            f'<rect x="{x+7*s}" y="{y+22*s}" width="{6*s}" height="{6*s}" fill="{W}"/><rect x="{x+27*s}" y="{y+22*s}" width="{6*s}" height="{6*s}" fill="{W}"/>')

def houses_vs():
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 150">']
    out.append(f'<rect x="0" y="0" width="110" height="150" fill="#FDE3E3"/>')
    out.append(f'<rect x="12" y="20" width="86" height="96" fill="{K}"/>')
    for r in range(5):
        for c in range(3):
            out.append(f'<rect x="{22+c*24}" y="{28+r*17}" width="14" height="10" fill="{Y}"/>')
    out.append(f'<text x="55" y="136" text-anchor="middle" font-family="Anton" font-size="14" fill="{R}">1 APÊ LEBLON</text>')
    out.append(f'<text x="128" y="80" font-family="Anton" font-size="30" fill="{K}">=</text>')
    for i in range(8):
        out.append(house(155 + (i % 4) * 66, 14 + (i // 4) * 56, 1.25, G, Y))
    out.append(f'<text x="285" y="142" text-anchor="middle" font-family="Anton" font-size="14" fill="{G}">QUASE 8,5 APÊS DE 3 QUARTOS EM COCHABAMBA</text>')
    out.append('</svg>')
    return "".join(out)

def car(x, y, s, color):
    return (f'<path d="M{x},{y+20*s} q0,-8 8,-9 l{14*s},-1 l{10*s},-10 h{30*s} l{14*s},10 l{14*s},2 q8,1 8,8 v6 h-{88*s} z" fill="{color}"/>'
            f'<circle cx="{x+20*s}" cy="{y+26*s}" r="{7*s}" fill="{K}"/><circle cx="{x+68*s}" cy="{y+26*s}" r="{7*s}" fill="{K}"/>'
            f'<path d="M{x+34*s},{y+9*s} l{8*s},-8 h{20*s} l{10*s},8 z" fill="#9fd3ff"/>')

def cars_vs():
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 120">']
    out.append(car(10, 30, 1.6, R))
    out.append(f'<text x="80" y="110" text-anchor="middle" font-family="Anton" font-size="14" fill="{R}">BRASIL: R$ 279.990</text>')
    out.append(f'<text x="185" y="70" font-family="Anton" font-size="30">=</text>')
    for i in range(4):
        out.append(car(215 + (i % 2) * 100, 8 + (i // 2) * 44, 0.95, G))
    out.append(f'<text x="315" y="114" text-anchor="middle" font-family="Anton" font-size="13" fill="{G}">4 MUSTANGS NA BOLÍVIA</text>')
    out.append('</svg>')
    return "".join(out)

def salt_flat():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 140">'
            f'<rect width="420" height="70" fill="#7EC8F2"/><rect y="70" width="420" height="70" fill="#E9F5FB"/>'
            f'<circle cx="340" cy="30" r="16" fill="{Y}"/>'
            f'<polygon points="0,70 60,38 110,70" fill="#8a7f9c"/><polygon points="90,70 170,30 240,70" fill="#a597b5"/>'
            f'<polygon points="0,70 60,102 110,70" fill="#8a7f9c" opacity=".35"/><polygon points="90,70 170,110 240,70" fill="#a597b5" opacity=".35"/>'
            f'<g stroke="#c9dbe5" stroke-width="1.5" fill="none"><path d="M10,90 l40,20 l60,-10 l50,25"/><path d="M200,85 l50,25 l70,-12 l60,22"/></g>'
            f'<g transform="translate(300,48)">{person(0,22,0.55,K,True)}</g>'
            f'<text x="20" y="130" font-family="Anton" font-size="14" fill="{B}">SALAR DE UYUNI · ilustração</text></svg>')

def esplanada():
    """Fundo da capa: céu de alerta, Congresso Nacional e Esplanada com multidão verde-amarela (ilustração própria)."""
    W_, H_ = 300, 425
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W_} {H_}" preserveAspectRatio="xMidYMid slice">',
         '<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#050505"/><stop offset=".45" stop-color="#2a0606"/>'
         '<stop offset=".72" stop-color="#8a1410"/><stop offset=".86" stop-color="#e0631c"/></linearGradient>'
         '<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".85"/>'
         '<stop offset=".5" stop-color="#000" stop-opacity=".25"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient></defs>',
         f'<rect width="{W_}" height="{H_}" fill="url(#sky)"/>']
    # Congresso: espelho d'água, plataforma, cúpulas e torres gêmeas
    o.append('<g fill="#0b0b0b">'
             '<rect x="20" y="300" width="260" height="12"/>'
             '<path d="M68,284 H140 A36,16 0 0 1 68,284 Z"/><rect x="100" y="298" width="8" height="4"/>'
             '<path d="M178,300 a22,11 0 0 1 44,0 z"/>'
             '<rect x="139" y="205" width="10" height="95"/><rect x="152" y="205" width="10" height="95"/>'
             '<rect x="139" y="232" width="23" height="4"/></g>')
    # bandeira no mastro
    o.append('<line x1="250" y1="196" x2="250" y2="300" stroke="#111" stroke-width="2"/>' + flag(250, 196, 30, wave=3))
    # Esplanada: blocos dos ministérios em perspectiva
    for i in range(6):
        x = 8 + i * 9
        o.append(f'<rect x="{x}" y="{292 - i*2}" width="6" height="{18 + i*2}" fill="#141414"/>')
        o.append(f'<rect x="{W_ - x - 6}" y="{292 - i*2}" width="6" height="{18 + i*2}" fill="#141414"/>')
    o.append('</svg>')
    svg = "".join(o)
    # multidão: reaproveita o gerador, recortada para a base
    c = crowd(w=600, h=200, seed=21, flags=14, signs=[("BRASIL ACIMA DE TUDO", 120), ("LIBERDADE!", 470)])
    inner = c[c.index(">") + 1:c.rindex("</svg>")]
    svg = svg.replace("</svg>", f'<g transform="translate(0,318) scale(0.5)">{inner}</g>'
                      f'<rect width="{W_}" height="{H_}" fill="url(#fade)"/></svg>')
    return svg

def palm(x, y, h, color="#120404"):
    """Palmeira imperial: tronco fino e copa em leque. (x,y) = base."""
    top = y - h
    o = [f'<path d="M{x-h*0.012},{y} L{x-h*0.006},{top} L{x+h*0.006},{top} L{x+h*0.012},{y} Z" fill="{color}"/>']
    for ang, ln in [(-160, .28), (-130, .3), (-100, .22), (-80, .22), (-50, .3), (-20, .28), (-180, .22), (0, .22)]:
        a = math.radians(ang)
        ex, ey = x + math.cos(a) * h * ln, top + math.sin(a) * h * ln * 0.55 + h * 0.06
        cx, cy = x + math.cos(a) * h * ln * 0.5, top - h * 0.07
        o.append(f'<path d="M{x},{top} Q{cx},{cy} {ex},{ey}" stroke="{color}" stroke-width="{max(0.6, h*0.022)}" fill="none" stroke-linecap="round"/>')
    return "".join(o)

def avenida():
    """Fundo da capa: avenida com palmeiras imperiais lotada de verde-amarelo, carro de som, céu de alerta."""
    random.seed(42)
    W_, H_, HZ, VX = 300, 425, 262, 205
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W_} {H_}" preserveAspectRatio="xMidYMid slice">',
         '<defs><linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0000"/>'
         '<stop offset=".35" stop-color="#3a0707"/><stop offset=".52" stop-color="#a8160f"/><stop offset=".615" stop-color="#ff7a1f"/></linearGradient>'
         '<linearGradient id="fade2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".8"/>'
         '<stop offset=".45" stop-color="#000" stop-opacity=".2"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>'
         '<linearGradient id="tint" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D7191C" stop-opacity=".0"/>'
         '<stop offset="1" stop-color="#5a0000" stop-opacity=".35"/></linearGradient></defs>',
         f'<rect width="{W_}" height="{H_}" fill="url(#sky2)"/>']
    # nuvens
    for cx, cy, r in [(60, 70, 40), (110, 55, 50), (170, 80, 36), (40, 130, 30), (95, 120, 42), (240, 150, 34), (270, 120, 28)]:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#5c0c0c" opacity=".55"/>')
    # árvores na linha do horizonte
    for i in range(70):
        x = random.uniform(0, W_); r = random.uniform(5, 13)
        o.append(f'<circle cx="{x:.1f}" cy="{HZ - r*0.4:.1f}" r="{r:.1f}" fill="#160505"/>')
    o.append(f'<rect x="0" y="{HZ}" width="{W_}" height="{H_-HZ}" fill="#3a2805"/>')
    # palmeiras imperiais em perspectiva, dos dois lados da avenida
    for side, base_x in [(1, 300), (-1, 120)]:
        for k in range(9):
            t = k / 9
            x = base_x + (VX - base_x) * (1 - (1 - t) ** 1.6) * 0.9
            y = 372 + (HZ + 4 - 372) * t
            h = 165 * (1 - t) ** 1.3 + 12
            o.append(palm(x, y, h))
    # mar de gente: cabeças em perspectiva
    cols = ["#FFDF00", "#FFDF00", "#009C3B", "#0b7a2f", "#2a1a0a", "#FFD60A", "#e8c800"]
    for i in range(6500):
        y = HZ + 2 + (H_ - HZ) * (random.random() ** 1.7)
        t = (y - HZ) / (H_ - HZ)
        x = random.uniform(-10, W_ + 10)
        r = 0.7 + t * 3.6
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{random.choice(cols)}"/>')
    # bandeiras na multidão
    for i in range(22):
        y = random.uniform(HZ + 15, H_ - 40); t = (y - HZ) / (H_ - HZ); w = 6 + t * 26
        x = random.uniform(0, W_ - w)
        o.append(f'<line x1="{x:.1f}" y1="{y + w*0.7:.1f}" x2="{x:.1f}" y2="{y + w*1.5:.1f}" stroke="#222" stroke-width="{0.4 + t:.1f}"/>' + flag(x, y, w, wave=w * 0.12))
    # carro de som (silhuetas de costas, sem rostos)
    o.append('<g fill="#0a0a0a">'
             '<path d="M-5,360 L95,345 L100,425 L-5,425 Z"/>'
             '<rect x="-5" y="318" width="102" height="4" transform="rotate(-8 45 320)"/>')
    for x, y, arm in [(18, 331, True), (40, 327, False), (62, 324, True), (82, 321, False)]:
        o.append(f'<circle cx="{x}" cy="{y-24}" r="6"/><path d="M{x-9},{y+14} v-22 q0,-6 9,-6 q9,0 9,6 v22 z"/>')
        if arm:
            o.append(f'<line x1="{x+7}" y1="{y-6}" x2="{x+13}" y2="{y-34}" stroke="#0a0a0a" stroke-width="3.5" stroke-linecap="round"/>')
    o.append('</g>')
    o.append(flag(66, 276, 34, wave=4))
    o.append('<line x1="66" y1="276" x2="64" y2="324" stroke="#0a0a0a" stroke-width="2"/>')
    o.append(f'<rect width="{W_}" height="{H_}" fill="url(#tint)"/><rect width="{W_}" height="{H_}" fill="url(#fade2)"/>')
    o.append('</svg>')
    return "".join(o)

files = {
    "crowd.svg": crowd(signs=[("BRASIL ACIMA DE TUDO", 140), ("LIBERDADE!", 460)]),
    "crowd-cover.svg": crowd(w=600, h=200, seed=3, flags=12, signs=[("MAIS 4 ANOS?", 470)], dark=True),
    "crowd-wide.svg": crowd(w=700, h=170, seed=11, flags=10, signs=[("DEUS, PÁTRIA, FAMÍLIA", 200), ("FORA COMUNISMO", 540)]),
    "flag.svg": big_flag(),
    "no-communism.svg": no_communism(),
    "route-map.svg": route_map(),
    "megaphone.svg": megaphone(),
    "houses-vs.svg": houses_vs(),
    "cars-vs.svg": cars_vs(),
    "salt-flat.svg": salt_flat(),
    "esplanada.svg": esplanada(),
    "avenida.svg": avenida(),
}
for n, s in files.items():
    (OUT / n).write_text(s, encoding="utf-8")
print("ok", list(files))
