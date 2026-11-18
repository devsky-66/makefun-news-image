# 17 November 2026 — The Day in One Image

[![make.fun bounty](https://make.fun/badge/news-image-20261117)](https://make.fun/bounty/news-image-20261117)

A single 1024×1024 infographic summing up the world news of
**Tuesday 17 November 2026**, drawn entirely in code — no AI-generated
imagery, so every word on the picture is crisp and legible.

## What is on the image

Six stories from 17 November 2026, across regions and fields:

1. **Ukraine war** — Ukraine struck the Kerch Bridge to Crimea for a second
   straight day; Russia hit two bridges in Kyiv.
2. **Middle East** — Iran fired drones at a US radar site in Bahrain;
   Bahrain said it intercepted them, with no casualties.
3. **Diplomacy** — China confirmed a three-way Xi–Trump–Putin summit in
   Shenzhen on Thursday 19 November, on the sidelines of APEC.
4. **Markets** — Wall Street slid on AI-valuation fears: the S&P 500 fell
   about 1% and the Dow lost about 850 points.
5. **Sport** — MS Dhoni retired from the IPL after 19 seasons and five
   titles; he will mentor Chennai Super Kings from 2027.
6. **Asia security** — Japan scrambled fighter jets after suspected Russian
   aircraft entered its airspace.

Facts were checked against reporting published on the day (Reuters, AP,
Al Jazeera, Times Now, Just Security). Nothing is invented: numbers are
rounded and marked "about", and claims are attributed to the party that
made them.

## How it works

- `draw_infographic.py` — draws `entry.png` with Pillow (build-time only;
  DejaVu Sans, bundled with most Linux systems). Re-run it to regenerate
  the image: `python3 draw_infographic.py`.
- `main.py` — the competition entry point. Python 3.13, standard library
  only, no network: it copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`),
  byte for byte, so two runs give identical output.
- `entry.png` — the finished image: 1024×1024 PNG, under 1 MiB.

## Verify locally

```sh
python3 draw_infographic.py
python3 -c "from PIL import Image; im = Image.open('entry.png'); print(im.size, im.format)"
mkdir -p /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png   # must match
```

## License

MIT — see [LICENSE](LICENSE).
