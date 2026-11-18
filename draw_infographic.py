#!/usr/bin/env python3
"""Draw the 17 November 2026 world-news infographic (1024x1024 PNG).

All news items were verified against reporting published on
17 November 2026 (Reuters, AP, Al Jazeera, Times Now, Just Security).
Run:  python3 draw_infographic.py   -> writes entry.png next to this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Palette: deep navy header, warm paper background, one accent per story.
NAVY = (13, 27, 62)
NAVY2 = (24, 48, 96)
PAPER = (247, 243, 235)
INK = (18, 22, 34)
GREY = (88, 92, 104)
WHITE = (255, 255, 255)
GOLD = (214, 158, 46)
RED = (178, 34, 34)

STORIES = [
    {
        "tag": "UKRAINE WAR",
        "accent": (178, 34, 34),
        "title": "Kerch Bridge hit again",
        "body": "Ukraine struck the bridge to Crimea for a second straight day; Russia hit two bridges in Kyiv.",
        "icon": "bridge",
    },
    {
        "tag": "MIDDLE EAST",
        "accent": (146, 90, 16),
        "title": "Iran drones target US radar",
        "body": "Iran fired drones at a US radar site in Bahrain; Bahrain said it intercepted them — no casualties.",
        "icon": "radar",
    },
    {
        "tag": "DIPLOMACY",
        "accent": (24, 86, 150),
        "title": "Xi, Trump and Putin to meet",
        "body": "China confirmed a three-way summit in Shenzhen on Thursday 19 November, on the sidelines of APEC.",
        "icon": "flags",
    },
    {
        "tag": "MARKETS",
        "accent": (34, 110, 60),
        "title": "Wall Street slides on AI fears",
        "body": "The S&P 500 fell about 1% and the Dow lost about 850 points as investors questioned AI valuations.",
        "icon": "chart",
    },
    {
        "tag": "SPORT",
        "accent": (120, 52, 140),
        "title": "Dhoni retires from the IPL",
        "body": "MS Dhoni ended his IPL playing career — 19 seasons, five titles — and will mentor Chennai from 2027.",
        "icon": "cricket",
    },
    {
        "tag": "ASIA SECURITY",
        "accent": (170, 80, 20),
        "title": "Japan scrambles jets",
        "body": "Japan launched fighter jets and protested after suspected Russian aircraft entered its airspace.",
        "icon": "jet",
    },
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_icon(d, kind, x, y, s, color):
    """Simple flat pictograms drawn with PIL primitives, inside a s x s box."""
    if kind == "bridge":
        d.line([(x, y + s * 0.62), (x + s, y + s * 0.62)], fill=color, width=7)
        d.arc([x + s * 0.08, y + s * 0.18, x + s * 0.92, y + s * 0.95],
              200, 340, fill=color, width=6)
        for fx in (0.22, 0.5, 0.78):
            d.line([(x + s * fx, y + s * 0.30), (x + s * fx, y + s * 0.62)],
                   fill=color, width=5)
        d.line([(x, y + s * 0.80), (x + s, y + s * 0.80)], fill=color, width=5)
    elif kind == "radar":
        d.ellipse([x + 4, y + 4, x + s - 4, y + s - 4], outline=color, width=6)
        d.ellipse([x + s * 0.28, y + s * 0.28, x + s * 0.72, y + s * 0.72],
                  outline=color, width=4)
        d.line([(x + s / 2, y + s / 2), (x + s * 0.86, y + s * 0.18)],
               fill=color, width=6)
        d.ellipse([x + s * 0.66, y + s * 0.62, x + s * 0.78, y + s * 0.74],
                  fill=color)
        d.ellipse([x + s * 0.20, y + s * 0.30, x + s * 0.30, y + s * 0.40],
                  fill=color)
    elif kind == "flags":
        for i, col in enumerate([(178, 34, 34), (24, 86, 150), (34, 110, 60)]):
            fx = x + i * s * 0.30
            d.line([(fx + s * 0.10, y + s * 0.08), (fx + s * 0.10, y + s * 0.88)],
                   fill=color, width=5)
            d.polygon([(fx + s * 0.10, y + s * 0.10), (fx + s * 0.42, y + s * 0.10),
                       (fx + s * 0.42, y + s * 0.42), (fx + s * 0.10, y + s * 0.42)],
                      fill=col)
    elif kind == "chart":
        d.line([(x + 4, y + s - 8), (x + s - 4, y + s - 8)], fill=color, width=5)
        d.line([(x + 4, y + s - 8), (x + 4, y + 6)], fill=color, width=5)
        pts = [(x + 8, y + s * 0.30), (x + s * 0.32, y + s * 0.42),
               (x + s * 0.55, y + s * 0.36), (x + s * 0.78, y + s * 0.62),
               (x + s - 6, y + s * 0.78)]
        d.line(pts, fill=color, width=7, joint="curve")
        d.polygon([(x + s - 6, y + s * 0.78), (x + s - 22, y + s * 0.72),
                   (x + s - 14, y + s * 0.88)], fill=color)
    elif kind == "cricket":
        d.rounded_rectangle([x + s * 0.30, y + s * 0.08, x + s * 0.62, y + s * 0.62],
                            radius=6, fill=color)
        d.rectangle([x + s * 0.40, y + s * 0.60, x + s * 0.52, y + s * 0.92],
                    fill=color)
        d.ellipse([x + s * 0.68, y + s * 0.66, x + s * 0.92, y + s * 0.90],
                  fill=(178, 34, 34))
    elif kind == "jet":
        # side view: fuselage as a thick line, swept wings as triangles
        d.line([(x + 4, y + s * 0.58), (x + s - 6, y + s * 0.38)],
               fill=color, width=10)
        d.polygon([(x + s * 0.42, y + s * 0.52), (x + s * 0.58, y + s * 0.10),
                   (x + s * 0.70, y + s * 0.46)], fill=color)
        d.polygon([(x + s * 0.30, y + s * 0.62), (x + s * 0.46, y + s * 0.90),
                   (x + s * 0.58, y + s * 0.60)], fill=color)
        d.polygon([(x + s * 0.78, y + s * 0.34), (x + s * 0.98, y + s * 0.30),
                   (x + s * 0.86, y + s * 0.48)], fill=color)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header ----
    d.rectangle([0, 0, W, 168], fill=NAVY)
    d.rectangle([0, 168, W, 176], fill=GOLD)
    f_date = font(FONT_BOLD, 52)
    f_sub = font(FONT_BOLD, 30)
    d.text((36, 34), "TUESDAY 17 NOVEMBER 2026", font=f_date, fill=WHITE)
    d.text((36, 108), "THE WORLD IN ONE IMAGE", font=f_sub, fill=GOLD)
    # globe mark top-right
    cx, cy, r = 952, 84, 40
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=5)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=None)
    d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=GOLD, width=4)
    d.line([(cx - r, cy), (cx + r, cy)], fill=GOLD, width=4)
    d.line([(cx, cy - r), (cx, cy + r)], fill=GOLD, width=4)

    # ---- story grid: 2 cols x 3 rows ----
    gx, gy = 28, 196
    cw, chh, gap = 472, 244, 24
    f_tag = font(FONT_BOLD, 22)
    f_title = font(FONT_BOLD, 33)
    f_body = font(FONT_REG, 22)
    for i, s in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = gx + col * (cw + gap)
        y0 = gy + row * (chh + gap)
        d.rounded_rectangle([x0, y0, x0 + cw, y0 + chh], radius=14,
                            fill=WHITE, outline=(205, 200, 188), width=2)
        d.rectangle([x0, y0, x0 + cw, y0 + 8], fill=s["accent"])
        # icon box
        ix, iy, isize = x0 + 18, y0 + 52, 84
        d.rounded_rectangle([ix, iy, ix + isize, iy + isize], radius=10,
                            fill=(238, 234, 224))
        draw_icon(d, s["icon"], ix + 10, iy + 10, isize - 20, s["accent"])
        # tag + title + body
        tx = ix + isize + 16
        d.text((tx, y0 + 18), s["tag"], font=f_tag, fill=s["accent"])
        title_lines = wrap(d, s["title"], f_title, cw - (tx - x0) - 18)
        ty = y0 + 50
        for ln in title_lines[:2]:
            d.text((tx, ty), ln, font=f_title, fill=INK)
            ty += 40
        body_lines = wrap(d, s["body"], f_body, cw - 36)
        by = y0 + 148
        for ln in body_lines[:3]:
            d.text((x0 + 18, by), ln, font=f_body, fill=(52, 56, 68))
            by += 28

    # ---- footer (single line, fits inside the canvas) ----
    fy = 196 + 3 * chh + 2 * gap + 14
    d.text((36, fy), "As reported on 17 November 2026  ·  Reuters · AP · Al Jazeera · Times Now · Just Security",
           font=font(FONT_REG, 21), fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    size = os.path.getsize(OUT)
    print(f"wrote {OUT}: {img.size[0]}x{img.size[1]}, {size} bytes "
          f"({'OK' if size <= 1048576 else 'TOO BIG'})")


if __name__ == "__main__":
    main()
