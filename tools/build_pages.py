"""Build the standalone GitHub Pages site in docs/ from the artifact page index.html.

index.html is written for claude.ai, which wraps it in its own document skeleton.
This script adds that skeleton plus what a home-screen web app needs: viewport,
web app manifest, theme colour and PNG icons.

Run from the repo root:  python3 tools/build_pages.py
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

BROWN = "#7A5034"
CREAM = "#FAF8F4"
SUN = "#E8C08A"
BG = "#f3efe8"

# Icon artwork on the 64-unit grid used by the in-app SVG
MOUNTAIN = [(6, 54), (30, 26), (42, 38), (48, 32), (58, 54)]
SUN_CENTER, SUN_R = (20, 22), 6


def icon(size: int, inset: float) -> Image.Image:
    """Full-bleed square icon; inset shrinks the artwork to keep it inside maskable safe zones."""
    ss = 4  # supersample for smooth edges
    big = size * ss
    img = Image.new("RGB", (big, big), BROWN)
    d = ImageDraw.Draw(img)
    scale = big * (1 - 2 * inset) / 64
    off = big * inset
    pt = lambda x, y: (off + x * scale, off + y * scale)
    d.polygon([pt(x, y) for x, y in MOUNTAIN], fill=CREAM)
    cx, cy = pt(*SUN_CENTER)
    r = SUN_R * scale
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SUN)
    return img.resize((size, size), Image.LANCZOS)


HEAD = """<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Uphill — บันทึกการเดินรายวัน ความชัน ความเร็ว เวลา คำนวณแคลอรี่ พร้อมความสำเร็จและรางวัล">
<meta name="theme-color" content="#f3efe8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#191613" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Uphill">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
"""


def main() -> None:
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    split = src.index('<div class="wrap"')
    page = HEAD + src[:split] + "</head>\n<body>\n" + src[split:] + "\n</body>\n</html>\n"

    DOCS.mkdir(exist_ok=True)
    (DOCS / "index.html").write_text(page, encoding="utf-8")
    (DOCS / ".nojekyll").write_text("")

    icon(180, 0.08).save(DOCS / "apple-touch-icon.png")
    icon(192, 0.12).save(DOCS / "icon-192.png")
    icon(512, 0.12).save(DOCS / "icon-512.png")

    manifest = {
        "name": "Uphill",
        "short_name": "Uphill",
        "description": "บันทึกการเดินรายวัน ความชัน ความเร็ว เวลา และแคลอรี่",
        "lang": "th",
        "start_url": "./",
        "scope": "./",
        "display": "standalone",
        "orientation": "portrait",
        "background_color": BG,
        "theme_color": BG,
        "icons": [
            {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
        ],
    }
    (DOCS / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {DOCS.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
