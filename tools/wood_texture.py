"""Procedural matte wood-grain plank texture (grain runs horizontally).
Usage: python3 -I wood.py OUT WIDTH HEIGHT PALETTE SEED
PALETTE: walnut | oak
"""
import sys
import numpy as np
from PIL import Image

out, W, H, pal, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5])
rng = np.random.default_rng(seed)


def noise(gw, gh, w=W, h=H):
    """Smooth value noise: random grid (gw x gh) upscaled bicubically to w x h."""
    g = rng.random((gh, gw)).astype(np.float32)
    im = Image.fromarray((g * 255).astype(np.uint8), "L").resize((w, h), Image.BICUBIC)
    return np.asarray(im).astype(np.float32) / 255.0


y = np.arange(H, dtype=np.float32)[:, None] * np.ones((1, W), np.float32)

# Long, gently wandering distortion -> grain lines that drift along the plank.
warp = (noise(6, 4) - 0.5) * 70 + (noise(18, 8) - 0.5) * 22 + (noise(60, 20) - 0.5) * 5
# Occasional "cathedral" swell
swell = (noise(3, 2) - 0.5) * 120

# Irregular ring spacing: integrate a noisy frequency down the plank.
freq = 2 * np.pi / (11 + 16 * noise(4, 10))
phase = np.cumsum(freq, axis=0) + (warp + swell) * freq
rings = 0.5 + 0.5 * np.sin(phase)
rings = rings ** 1.8  # thinner dark latewood lines
rings *= 0.55 + 0.45 * noise(30, 12)  # lines fade in and out

fiber = noise(W // 9, H // 2) * 0.5 + noise(W // 3, H) * 0.3 + noise(W // 40, H // 3) * 0.2
broad = noise(5, 3)  # large tonal variation

t = np.clip(0.36 * (1 - rings) + 0.34 * fiber + 0.36 * broad - 0.02, 0, 1)

if pal == "walnut":
    dark = np.array([36, 23, 15], np.float32)
    mid = np.array([80, 52, 33], np.float32)
    light = np.array([118, 80, 52], np.float32)
else:  # oak / honey
    dark = np.array([132, 94, 60], np.float32)
    mid = np.array([174, 133, 92], np.float32)
    light = np.array([204, 167, 124], np.float32)

t3 = t[..., None]
col = np.where(t3 < 0.5, dark + (mid - dark) * (t3 / 0.5), mid + (light - mid) * ((t3 - 0.5) / 0.5))

# Matte: very light grain-sized speckle, no specular highlight.
col *= (0.97 + 0.06 * rng.random((H, W, 1)).astype(np.float32))
img = Image.fromarray(np.clip(col, 0, 255).astype(np.uint8), "RGB")
img.save(out, "JPEG", quality=80, optimize=True, progressive=True)
print(out, img.size)
