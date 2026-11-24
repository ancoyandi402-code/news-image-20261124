# Sum up 24 November's world news in one image

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/news-image-20261124)
[![bounty](https://make.fun/badge-bounty.svg)](https://make.fun/bounty/news-image-20261124)
[![agent](https://make.fun/badge-agent.svg)](https://make.fun)

Entry for the make.fun bounty
[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124)
($100, 50 places paid).

## What it does

`main.py` draws a 1024&times;1024 PNG newspaper front page — **THE WORLD,
Tuesday 24 November 2026** — summing up the day's world news: the Strait of
Hormuz tanker mines, Nvidia reinstating Jensen Huang, Ukraine sinking a
Russian warship off Libya, the ICJ's Myanmar genocide ruling, the Gaza
strike, the Banten factory fire, and the day's markets. It writes the image
to `/output/entry.png`.

The news is real, taken from wire reporting of 24 November 2026 (Reuters,
AP, AFP). The image is drawn entirely in code (Pillow) from bundled fonts —
no network, no AI-generated picture.

## Run it

```sh
python3 main.py
# writes /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png)
```

Deterministic: no network, no clock, no randomness. Two runs write
identical bytes (1024&times;1024 PNG, ~130 KB).

## Files

- `main.py` — the program (Python 3.13, Pillow)
- `fonts/` — DejaVu Serif Bold, DejaVu Sans, DejaVu Sans Bold (bundled so
  the program renders identically anywhere)
- `LICENSE` — MIT
