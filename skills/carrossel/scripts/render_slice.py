#!/usr/bin/env python
"""Render a carousel HTML and slice it into N square-ish slides.

Usage:
    python render_slice.py <carrossel.html> <out_dir> [n_slides=7] [slide_w=1080] [slide_h=1350]

Renders the HTML with headless Chrome at (slide_w x n*slide_h), screenshots the full
stack, then slices into slide-1.png .. slide-N.png (slide_w x slide_h each) with PIL.
Run with PYTHONUTF8=1 to avoid cp1252 crashes on Windows.
"""
import sys, subprocess, tempfile, os
from pathlib import Path

def find_chrome():
    cands = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/usr/bin/google-chrome", "/usr/bin/chromium-browser", "/usr/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for c in cands:
        if Path(c).exists():
            return c
    raise SystemExit("Chrome not found — edit find_chrome() with your path.")

def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    html = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]); out_dir.mkdir(parents=True, exist_ok=True)
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    W = int(sys.argv[4]) if len(sys.argv) > 4 else 1080
    H = int(sys.argv[5]) if len(sys.argv) > 5 else 1350
    total_h = n * H

    chrome = find_chrome()
    full_png = Path(tempfile.gettempdir()) / "ultracarrossel-full.png"
    url = "file:///" + str(html).replace("\\", "/")
    cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", f"--window-size={W},{total_h}",
           "--virtual-time-budget=16000", f"--screenshot={full_png}", url]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    if not full_png.exists():
        raise SystemExit(f"Chrome did not produce {full_png}")

    from PIL import Image
    src = Image.open(full_png).convert("RGB")
    sw, sh = src.size
    # If Chrome rendered at a different total height, scale to expected.
    if (sw, sh) != (W, total_h):
        src = src.resize((W, total_h))
    for i in range(n):
        crop = src.crop((0, i * H, W, (i + 1) * H))
        if crop.size != (W, H):
            crop = crop.resize((W, H))
        p = out_dir / f"slide-{i+1}.png"
        crop.save(p)
        print(f"  {p.name}  {crop.size}")
    print(f"OK -> {out_dir}")

if __name__ == "__main__":
    main()
