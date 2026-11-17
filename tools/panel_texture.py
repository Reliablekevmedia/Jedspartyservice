"""Matte-black architectural wall panels as a seamless SVG tile (vector, so it stays crisp).

Large panels in a stacked grid with recessed joints ("reveals"): a dark groove, a fine
highlight where the light catches the panel edge, and a slight tone shift from panel to panel.

Usage: python3 tools/panel_texture.py website/public/img/black-panels.svg
"""
import random
import sys

COLS, ROWS = 3, 2          # panels per tile (tile repeats seamlessly)
PW, PH = 480, 360          # panel size in CSS px at 1x
REVEAL = 3                 # joint width
W, H = COLS * PW, ROWS * PH

rng = random.Random(7)
parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<defs>",
    # light falls from above: each panel is a touch brighter at the top
    '<linearGradient id="fall" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0" stop-color="#fff" stop-opacity=".028"/>'
    '<stop offset=".55" stop-color="#fff" stop-opacity="0"/>'
    '<stop offset="1" stop-color="#000" stop-opacity=".14"/></linearGradient>',
    # soft shadow just below each horizontal joint, as if the panel sits slightly proud
    '<linearGradient id="lip" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0" stop-color="#000" stop-opacity=".35"/>'
    '<stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>',
    "</defs>",
]

for r in range(ROWS):
    for c in range(COLS):
        x, y = c * PW, r * PH
        tone = rng.uniform(-0.05, 0.03)  # panel-to-panel variation
        fill = "#fff" if tone > 0 else "#000"
        parts.append(f'<rect x="{x}" y="{y}" width="{PW}" height="{PH}" fill="{fill}" fill-opacity="{abs(tone):.3f}"/>')
        parts.append(f'<rect x="{x}" y="{y}" width="{PW}" height="{PH}" fill="url(#fall)"/>')
        parts.append(f'<rect x="{x}" y="{y + REVEAL}" width="{PW}" height="10" fill="url(#lip)"/>')

for r in range(ROWS):  # horizontal joints
    y = r * PH
    parts.append(f'<rect x="0" y="{y}" width="{W}" height="{REVEAL}" fill="#060504"/>')
    parts.append(f'<rect x="0" y="{y + REVEAL}" width="{W}" height="1" fill="#fff" fill-opacity=".07"/>')
    parts.append(f'<rect x="0" y="{y + PH - 1}" width="{W}" height="1" fill="#fff" fill-opacity=".035"/>')
for c in range(COLS):  # vertical joints
    x = c * PW
    parts.append(f'<rect x="{x}" y="0" width="{REVEAL}" height="{H}" fill="#060504"/>')
    parts.append(f'<rect x="{x + REVEAL}" y="0" width="1" height="{H}" fill="#fff" fill-opacity=".05"/>')
    parts.append(f'<rect x="{x + PW - 1}" y="0" width="1" height="{H}" fill="#000" fill-opacity=".45"/>')

parts.append("</svg>")
open(sys.argv[1], "w").write("\n".join(parts) + "\n")
print(sys.argv[1], f"{W}x{H}")
