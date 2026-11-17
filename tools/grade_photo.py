"""Warm matte grade: mute cool/purple casts, keep warm (amber/red) tones,
lift blacks and soften whites for a matte finish. Usage:
    python3 -I grade.py SRC DST [max_width] [crop=x0,y0,x1,y1 fractions]
"""
import sys
import numpy as np
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
max_w = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
crop = sys.argv[4] if len(sys.argv) > 4 else None

im = Image.open(src).convert("RGB")
if crop:
    fx0, fy0, fx1, fy1 = (float(v) for v in crop.split(","))
    w, h = im.size
    im = im.crop((int(fx0 * w), int(fy0 * h), int(fx1 * w), int(fy1 * h)))
if im.width > max_w:
    im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)

if len(sys.argv) > 5 and sys.argv[5] == "mono":
    # Warm duotone: matte black -> ivory, for photos with heavy coloured lighting
    lum = np.asarray(im.convert("L")).astype(np.float32) / 255.0
    lum = np.clip(0.5 + (lum - 0.5) * 1.12, 0, 1) ** 0.95
    lo = np.array([30, 24, 20], np.float32); hi = np.array([242, 232, 216], np.float32)
    out = Image.fromarray((lo + (hi - lo) * lum[..., None]).astype(np.uint8), "RGB")
    out.save(dst, "JPEG", quality=84, optimize=True, progressive=True)
    print(dst, out.size, "mono")
    sys.exit(0)

hsv = np.asarray(im.convert("HSV")).astype(np.float32)
hue = hsv[..., 0] * 360.0 / 255.0

# Saturation multiplier by hue: warm keeps colour, cool goes to near-mono.
def smooth(x, a, b):
    t = np.clip((x - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)

warm = np.maximum(1 - smooth(hue, 45, 75), smooth(hue, 335, 355))  # reds/oranges/ambers
mult = 0.06 + warm * 0.74
hsv[..., 1] *= mult
graded = Image.fromarray(hsv.astype(np.uint8), "HSV").convert("RGB")

rgb = np.asarray(graded).astype(np.float32) / 255.0
# slight contrast, then matte lift (raised blacks, softened whites)
rgb = 0.5 + (rgb - 0.5) * 1.06
rgb = 0.055 + np.clip(rgb, 0, 1) * 0.89
# warm tint
rgb[..., 0] *= 1.035
rgb[..., 1] *= 1.0
rgb[..., 2] *= 0.93
out = Image.fromarray((np.clip(rgb, 0, 1) * 255).astype(np.uint8), "RGB")
out.save(dst, "JPEG", quality=82, optimize=True, progressive=True)
print(dst, out.size)
