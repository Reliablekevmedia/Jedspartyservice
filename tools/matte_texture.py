"""Seamless matte-black texture tile (powder-coat / honed-stone feel).
Usage: python3 matte.py OUT.jpg SIZE SEED
"""
import sys

import numpy as np
from PIL import Image

out, N, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)

fy = np.fft.fftfreq(N)[:, None]
fx = np.fft.fftfreq(N)[None, :]
f = np.hypot(fx, fy)


def band(lo_px, hi_px):
    """Periodic noise containing features between lo_px and hi_px in size (FFT => tiles seamlessly)."""
    white = rng.standard_normal((N, N))
    spec = np.fft.fft2(white)
    lo, hi = 1.0 / hi_px, 1.0 / lo_px
    mask = np.exp(-((np.log(f + 1e-9) - np.log(np.sqrt(lo * hi))) ** 2) / (2 * (np.log(hi / lo) / 2.2) ** 2))
    n = np.real(np.fft.ifft2(spec * mask))
    return n / n.std()


grain = band(1, 3)        # fine tooth of the finish
speck = band(3, 9)        # soft speckle
mottle = band(24, 90)     # cloudy variation
drift = band(120, 512)    # broad tonal drift

lum = 3.0 * grain + 1.7 * speck + 2.0 * mottle + 1.3 * drift
# sparse light flecks, like a stone/powder finish
flecks = (rng.random((N, N)) > 0.9975) * rng.uniform(4, 9, (N, N))
lum = lum + flecks

base = np.array([21, 19, 17], np.float32)  # warm matte black
tint = np.array([1.0, 0.95, 0.88], np.float32)
img = base + lum[..., None] * tint
Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB").save(out, "JPEG", quality=90, optimize=True, progressive=True)
print(out, N, f"lum std {lum.std():.2f}")
