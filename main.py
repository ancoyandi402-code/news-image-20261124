#!/usr/bin/env python3
"""Sum up 24 November 2026 world news in one image.

Writes a 1024x1024 PNG newspaper front page to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png). Deterministic: no network, no clock,
no randomness -- the same bytes come out on every run.

News: the top world stories of Tuesday 24 November 2026, as reported by
Reuters / AP / AFP and summarised by wire desks that day.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (250, 247, 240)      # newsprint off-white
INK = (18, 18, 18)        # near-black
RED = (155, 28, 28)       # kicker red
GREY = (90, 88, 82)
MARGIN = 44
CW = W - 2 * MARGIN        # content width: 936

HERE = os.path.dirname(os.path.abspath(__file__))


def font(name, size):
    """Load a bundled font (fonts/ first, then beside this file)."""
    for path in (os.path.join(HERE, "fonts", name),
                 os.path.join(HERE, name)):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.truetype(name, size)


F_SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_SANS = lambda s: font("DejaVuSans.ttf", s)
F_SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Wrap text to lines that fit max_w pixels. Returns a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, lines, fnt, fill=INK, leading=1.25):
    """Draw lines centred on the page. Returns y below the block."""
    for line in lines:
        draw.text((W / 2, y), line, font=fnt, fill=fill, anchor="ma")
        y += int(fnt.size * leading)
    return y


def draw_block(draw, x, y, width, kicker, headline, summary,
               k_size=20, h_size=28, s_size=20, align="left"):
    """One news item: kicker, headline, summary. Returns y below it."""
    fk, fh, fs = F_SANS_B(k_size), F_SERIF_B(h_size), F_SANS(s_size)
    anchor = "la" if align == "left" else "ma"
    tx = x if align == "left" else x + width / 2
    draw.text((tx, y), kicker, font=fk, fill=RED, anchor=anchor)
    y += int(k_size * 1.5)
    for line in wrap(draw, headline, fh, width):
        draw.text((tx, y), line, font=fh, fill=INK, anchor=anchor)
        y += int(h_size * 1.18)
    y += 4
    for line in wrap(draw, summary, fs, width):
        draw.text((tx, y), line, font=fs, fill=INK, anchor=anchor)
        y += int(s_size * 1.3)
    return y


def rule(draw, y, weight=1):
    draw.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=weight)
    return y + weight


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    y = 28
    d.text((W / 2, y), "THE WORLD", font=F_SERIF_B(88), fill=INK, anchor="ma")
    y = 28 + 98
    y = rule(d, y, 4)
    y = rule(d, y + 5, 1)
    y += 10
    d.text((W / 2, y), "TUESDAY, 24 NOVEMBER 2026  \u2022  THE WORLD IN ONE PAGE",
           font=F_SANS_B(22), fill=INK, anchor="ma")
    y += 30
    y = rule(d, y, 1)
    y += 14

    # ---- Lead story: Strait of Hormuz ----
    fk = F_SANS_B(24)
    d.text((W / 2, y), "STRAIT OF HORMUZ", font=fk, fill=RED, anchor="ma")
    y += 34
    y = draw_centered(d, y, wrap(d, "IRAN SAYS TANKERS HIT MINES AS STRAIT CLOSES",
                                 F_SERIF_B(48), CW), F_SERIF_B(48), leading=1.1)
    y += 6
    y = draw_centered(d, y, wrap(d, "Four tankers struck mines in the strait, Tehran says, as its "
                                  "army chief orders the waterway shut until Washington meets "
                                  "Iran's conditions.", F_SANS(24), CW - 60),
                      F_SANS(24), leading=1.28)
    y += 12
    y = rule(d, y, 1)
    y += 14

    # ---- Secondary stories: 2 x 2 grid ----
    col_w = (CW - 24) // 2
    x0, x1 = MARGIN, MARGIN + col_w + 24
    stories = [
        ("MARKETS", "Huang back as Nvidia chief; shares soar 31%",
         "Board reinstates Jensen Huang as CEO after pressure from Trump; "
         "S&P 500 jumps 4.73%."),
        ("UKRAINE", "Ukraine sinks Russian warship off Libya",
         "Kyiv says seven naval drones sank the corvette Merkury at Benghazi. "
         "Zelensky confirms."),
        ("THE HAGUE", "World court: Myanmar guilty of Rohingya genocide",
         "ICJ finds Myanmar guilty of genocide against the Rohingya; "
         "a precedent for Gaza."),
        ("GAZA", "Israel kills Hamas security chief in Gaza",
         "Israeli strike kills Brig. Gen. Naeem Abu Nahel, Hamas's security "
         "chief, and six others."),
    ]
    row_y = y
    y1 = draw_block(d, x0, row_y, col_w, *stories[0])
    y2 = draw_block(d, x1, row_y, col_w, *stories[1])
    row_y = max(y1, y2) + 14
    y1 = draw_block(d, x0, row_y, col_w, *stories[2])
    y2 = draw_block(d, x1, row_y, col_w, *stories[3])
    y = max(y1, y2) + 12
    y = rule(d, y, 1)
    y += 12

    # ---- Bottom story: Indonesia (full width) ----
    y = draw_block(d, MARGIN, y, CW,
                   "INDONESIA", "Banten factory fire kills 26",
                   "A factory fire in Banten, Indonesia, kills 26 people, with dozens "
                   "still missing, officials say.",
                   k_size=20, h_size=28, s_size=20, align="left")
    y += 12

    # ---- Markets strip ----
    strip_h = 48
    d.rectangle([MARGIN, y, W - MARGIN, y + strip_h], outline=INK, width=2)
    d.text((W / 2, y + strip_h / 2), "MARKETS  \u2022  S&P 500 7,237 \u25b2 4.73%  \u2022  "
           "Nikkei 225 \u25b2 3.91%  \u2022  Brent $86.71",
           font=F_SANS_B(19), fill=INK, anchor="mm")
    y += strip_h + 12

    # ---- Footer ----
    d.text((W / 2, y), "Compiled from wire reports \u2014 Reuters, AP, AFP",
           font=F_SANS(17), fill=GREY, anchor="ma")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    img.save(path, format="PNG")
    print("wrote", path, img.size)


if __name__ == "__main__":
    main()
