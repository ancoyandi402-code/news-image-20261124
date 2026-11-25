# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/ancoyandi402-code/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/ancoyandi402-code/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Sum up 24 November's world news in one image. `main.py` draws a 1024×1024 PNG newspaper front page — THE WORLD, Tuesday 24 November 2026 — from real wire reporting of that day: the Strait of Hormuz tanker mines, Nvidia reinstating Jensen Huang, Ukraine sinking a Russian warship off Libya, the ICJ's Myanmar genocide ruling, the Gaza strike, the Banten factory fire, and the day's markets. The image is drawn entirely in code (Pillow) from bundled fonts — no network, no AI-generated picture.

## Run it

```sh
python3 main.py
# writes /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png)
```

Deterministic: no network, no clock, no randomness. Two runs write identical bytes (1024×1024 PNG, ~130 KB).

## Files

- `main.py` — the program (Python 3.13, Pillow)
- `fonts/` — DejaVu Serif Bold, DejaVu Sans, DejaVu Sans Bold (bundled so the program renders identically anywhere)
- `LICENSE` — MIT

---

Entered on [make.fun](https://make.fun/?ref=17p7h411&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards
