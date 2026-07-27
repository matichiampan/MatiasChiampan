#!/usr/bin/env python3
"""Genera las seis placas editables del carrusel de Seguridad PBA."""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path("carousel")
W, H = 1080, 1350
BG, INK, RED, GREEN, WHITE = "#b7b6b7", "#111111", "#d92f35", "#168b55", "#ffffff"


def lines(text, x, y, size, weight=700, fill=INK, gap=1.04, anchor="start", italic=False):
    rows = text.split("\n")
    style = "italic" if italic else "normal"
    return "\n".join(
        f'<text x="{x}" y="{y + i * size * gap:.0f}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" text-anchor="{anchor}" font-style="{style}">{escape(row)}</text>'
        for i, row in enumerate(rows)
    )


def base(number, kicker="SEGURIDAD · PBA"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="1080" height="1350" fill="{BG}"/>
  <style>text {{ font-family: 'DejaVu Sans', Arial, sans-serif; }}</style>
  <text x="72" y="75" font-size="22" font-weight="700" letter-spacing="2">{kicker}</text>
  <text x="1008" y="75" font-size="20" font-weight="700" text-anchor="end">{number}/6</text>
  <line x1="72" y1="102" x2="1008" y2="102" stroke="#111" stroke-width="2"/>
'''


def footer():
    return '''  <g transform="translate(72 1262)">
    <circle cx="7" cy="-7" r="7" fill="#ff6b2c"/><circle cx="24" cy="-7" r="7" fill="#ff6b2c"/><circle cx="15.5" cy="-22" r="7" fill="#ff6b2c"/>
    <text x="42" y="0" font-size="26" font-weight="800">afiches</text>
  </g>
</svg>'''


slides = []

# 1 — apertura
s = base(1)
s += lines("¿QUÉ PASA CUANDO\nLA INSEGURIDAD\nDEJA DE SER\nUNA SENSACIÓN?", 72, 230, 77, 800, gap=.98)
s += f'<rect x="72" y="610" width="936" height="4" fill="{INK}"/>'
s += lines("37%", 72, 805, 185, 800, RED)
s += lines("de los hogares bonaerenses sufrió\nun hecho de inseguridad en el último año.", 82, 890, 37, 700, gap=1.22)
s += lines("Deslizá para ver qué cambia después.", 72, 1150, 26, 500)
s += footer(); slides.append(s)

# 2 — dimensión y preocupación
s = base(2)
s += lines("EL MIEDO YA FORMA PARTE\nDE LA VIDA COTIDIANA", 72, 220, 62, 800)
s += lines("51%", 72, 505, 150, 800, RED)
s += lines("se siente poco o nada seguro\nen su propio barrio.", 82, 580, 35, 700, gap=1.2)
s += f'<rect x="72" y="745" width="936" height="282" rx="20" fill="{INK}"/>'
s += lines("¿Qué preocupa más?", 112, 810, 28, 600, WHITE)
s += lines("50%", 112, 930, 92, 800, WHITE)
s += lines("ROBOS Y ASALTOS", 400, 909, 39, 800, WHITE)
s += lines("Muy por encima de hurtos, drogas,\nfalta de policía y violencia con armas.", 400, 961, 24, 400, BG, gap=1.25)
s += footer(); slides.append(s)

# 3 — territorio
s = base(3)
s += lines("NO SE VIVE IGUAL\nEN TODA LA PROVINCIA", 72, 220, 66, 800)
s += lines("El Conurbano combina más victimización\ny una sensación de inseguridad más alta.", 72, 385, 29, 500, gap=1.28)
s += lines("41%", 72, 655, 112, 800, INK)
s += lines("fue víctima", 78, 715, 27, 700)
s += lines("31%", 635, 655, 112, 800, INK)
s += lines("RESTO PBA", 642, 715, 27, 700)
s += f'<line x1="540" y1="530" x2="540" y2="770" stroke="{INK}" stroke-width="2"/>'
s += lines("63%", 72, 960, 112, 800, RED)
s += lines("se siente inseguro", 78, 1020, 27, 700)
s += lines("41%", 635, 960, 112, 800, RED)
s += lines("CONURBANO", 72, 1142, 22, 800)
s += lines("RESTO PBA", 635, 1142, 22, 800)
s += footer(); slides.append(s)

# 4 — cruce victimización / sensación
s = base(4, "EL EFECTO DE SER VÍCTIMA")
s += lines("DESPUÉS DE UN HECHO,\nLA PERCEPCIÓN CAMBIA", 72, 220, 64, 800)
s += lines("72%", 72, 560, 176, 800, RED)
s += lines("de las víctimas se siente\npoco o nada segura.", 82, 650, 38, 700, gap=1.18)
s += f'<rect x="72" y="810" width="936" height="204" rx="20" fill="{WHITE}" fill-opacity=".78"/>'
s += lines("33 PUNTOS", 112, 900, 64, 800, INK)
s += lines("Es la brecha frente a quienes no fueron víctimas:\nentre ellas, la inseguridad baja al 39%.", 112, 952, 24, 500, gap=1.3)
s += lines("La experiencia personal transforma el miedo.", 72, 1135, 27, 600)
s += footer(); slides.append(s)

# 5 — producto diferencial / cualitativo
s = base(5, "ENTREVISTAS GUIADAS CON IA")
s += lines("PERO LO MÁS IMPORTANTE:", 72, 210, 31, 800)
s += lines("LO MEDIMOS EN LAS\nPROPIAS PALABRAS\nDE LAS PERSONAS", 72, 290, 64, 800, RED, gap=1.03)
s += f'<rect x="72" y="575" width="936" height="382" rx="22" fill="{INK}"/>'
s += lines("“Volvíamos del club y unos chicos", 112, 660, 30, 700, WHITE)
s += lines("en moto nos arrebataron las", 112, 705, 30, 700, WHITE)
s += lines("riñoneras. Lo peor fue perder las", 112, 750, 30, 700, WHITE)
s += lines("llaves de casa; esa noche", 112, 795, 30, 700, WHITE)
s += lines("dormimos muy asustados.”", 112, 840, 30, 700, WHITE)
s += lines("MUJER · 45–59 · MORÓN · CONURBANO", 112, 912, 17, 700, BG)
s += lines("Nuestro entrevistador IA combina profundidad cualitativa\ncon una escala cuantitativa: no solo cuánto, también por qué.", 72, 1035, 25, 600, gap=1.3)
s += footer(); slides.append(s)

# 6 — CTA
s = base(6, "INFORME SEGURIDAD · PBA")
s += lines("¿QUERÉS VER\nEL INFORME\nCOMPLETO?", 72, 275, 86, 800, gap=.98)
s += f'<rect x="72" y="620" width="936" height="360" rx="28" fill="{INK}"/>'
s += lines("COMENTÁ", 540, 755, 92, 800, WHITE, anchor="middle")
s += lines("LA PUBLICACIÓN", 540, 860, 58, 800, BG, anchor="middle")
s += lines("y te lo enviamos.", 540, 930, 30, 500, WHITE, anchor="middle")
s += lines("Opinión pública + análisis de mercado + entrevistas con IA", 540, 1100, 22, 600, anchor="middle")
s += footer(); slides.append(s)

OUT.mkdir(exist_ok=True)
for i, content in enumerate(slides, 1):
    (OUT / f"{i:02d}.svg").write_text(content, encoding="utf-8")
print(f"Generadas {len(slides)} placas en {OUT}/")
