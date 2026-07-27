#!/usr/bin/env python3
"""Renderiza los SVG simples del carrusel a PNG usando la libcairo del sistema."""

import ctypes
import math
from pathlib import Path
import xml.etree.ElementTree as ET


cairo = ctypes.CDLL("libcairo.so.2")
P = ctypes.c_void_p
for name, args in {
    "cairo_image_surface_create": [ctypes.c_int, ctypes.c_int, ctypes.c_int],
    "cairo_create": [P], "cairo_destroy": [P], "cairo_surface_destroy": [P],
    "cairo_new_path": [P], "cairo_close_path": [P], "cairo_fill": [P], "cairo_stroke": [P],
    "cairo_set_source_rgb": [P, ctypes.c_double, ctypes.c_double, ctypes.c_double],
    "cairo_set_source_rgba": [P, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double],
    "cairo_rectangle": [P, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double],
    "cairo_move_to": [P, ctypes.c_double, ctypes.c_double], "cairo_line_to": [P, ctypes.c_double, ctypes.c_double],
    "cairo_arc": [P, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double],
    "cairo_set_line_width": [P, ctypes.c_double], "cairo_select_font_face": [P, ctypes.c_char_p, ctypes.c_int, ctypes.c_int],
    "cairo_set_font_size": [P, ctypes.c_double], "cairo_show_text": [P, ctypes.c_char_p],
    "cairo_translate": [P, ctypes.c_double, ctypes.c_double],
}.items():
    getattr(cairo, name).argtypes = args
cairo.cairo_image_surface_create.restype = P
cairo.cairo_create.restype = P
cairo.cairo_surface_write_to_png.argtypes = [P, ctypes.c_char_p]


class Extents(ctypes.Structure):
    _fields_ = [(n, ctypes.c_double) for n in ("x_bearing", "y_bearing", "width", "height", "x_advance", "y_advance")]


cairo.cairo_text_extents.argtypes = [P, ctypes.c_char_p, ctypes.POINTER(Extents)]


def color(value):
    value = value.lstrip("#")
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    return tuple(int(value[i:i + 2], 16) / 255 for i in (0, 2, 4))


def source(ctx, value, alpha=1):
    cairo.cairo_set_source_rgba(ctx, *color(value), alpha)


def rounded_rect(ctx, x, y, w, h, radius):
    radius = min(radius, w / 2, h / 2)
    cairo.cairo_new_path(ctx)
    cairo.cairo_arc(ctx, x + w - radius, y + radius, radius, -math.pi / 2, 0)
    cairo.cairo_arc(ctx, x + w - radius, y + h - radius, radius, 0, math.pi / 2)
    cairo.cairo_arc(ctx, x + radius, y + h - radius, radius, math.pi / 2, math.pi)
    cairo.cairo_arc(ctx, x + radius, y + radius, radius, math.pi, 3 * math.pi / 2)
    cairo.cairo_close_path(ctx)


def draw(ctx, node, dx=0, dy=0):
    tag = node.tag.rsplit("}", 1)[-1]
    a = node.attrib
    if tag == "g":
        transform = a.get("transform", "")
        if transform.startswith("translate("):
            values = transform[10:-1].replace(",", " ").split()
            dx += float(values[0]); dy += float(values[1] if len(values) > 1 else 0)
        for child in node:
            draw(ctx, child, dx, dy)
    elif tag == "rect":
        x, y = float(a.get("x", 0)) + dx, float(a.get("y", 0)) + dy
        w, h, radius = float(a["width"]), float(a["height"]), float(a.get("rx", 0))
        rounded_rect(ctx, x, y, w, h, radius) if radius else cairo.cairo_rectangle(ctx, x, y, w, h)
        source(ctx, a["fill"], float(a.get("fill-opacity", 1))); cairo.cairo_fill(ctx)
    elif tag == "circle":
        source(ctx, a["fill"]); cairo.cairo_arc(ctx, float(a["cx"]) + dx, float(a["cy"]) + dy, float(a["r"]), 0, 2 * math.pi); cairo.cairo_fill(ctx)
    elif tag == "line":
        source(ctx, a["stroke"]); cairo.cairo_set_line_width(ctx, float(a.get("stroke-width", 1)))
        cairo.cairo_move_to(ctx, float(a["x1"]) + dx, float(a["y1"]) + dy); cairo.cairo_line_to(ctx, float(a["x2"]) + dx, float(a["y2"]) + dy); cairo.cairo_stroke(ctx)
    elif tag == "text":
        text = (node.text or "").encode()
        slant = 1 if a.get("font-style") == "italic" else 0
        weight = 1 if int(a.get("font-weight", 400)) >= 600 else 0
        cairo.cairo_select_font_face(ctx, b"DejaVu Sans", slant, weight); cairo.cairo_set_font_size(ctx, float(a["font-size"]))
        source(ctx, a.get("fill", "#111111"))
        x, y = float(a["x"]) + dx, float(a["y"]) + dy
        if a.get("text-anchor") == "middle":
            ext = Extents(); cairo.cairo_text_extents(ctx, text, ctypes.byref(ext)); x -= ext.width / 2 + ext.x_bearing
        elif a.get("text-anchor") == "end":
            ext = Extents(); cairo.cairo_text_extents(ctx, text, ctypes.byref(ext)); x -= ext.width + ext.x_bearing
        cairo.cairo_move_to(ctx, x, y); cairo.cairo_show_text(ctx, text)


def render(svg, png):
    root = ET.parse(svg).getroot()
    surface = cairo.cairo_image_surface_create(0, int(root.attrib["width"]), int(root.attrib["height"]))
    ctx = cairo.cairo_create(surface)
    for node in root:
        draw(ctx, node)
    cairo.cairo_surface_write_to_png(surface, str(png).encode())
    cairo.cairo_destroy(ctx); cairo.cairo_surface_destroy(surface)


if __name__ == "__main__":
    for svg in sorted(Path("carousel").glob("*.svg")):
        render(svg, svg.with_suffix(".png"))
        print(f"Generado {svg.with_suffix('.png')}")
