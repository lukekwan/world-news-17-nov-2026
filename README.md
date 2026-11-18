# The World — Tuesday 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/lukekwan/world-news-17-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/lukekwan/world-news-17-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world's news of Tuesday 17 November 2026, in
the form of a dark breaking-news poster.

**Design:** deep navy background, a red BREAKING banner with the date, a
large radar visual sweeping over the Gulf with a marker on Sheikh Isa
base, and the lead headline set huge: IRAN STRIKES U.S. RADAR IN BAHRAIN.

**Lead:** Iran strikes a U.S. radar in Bahrain — drones hit the Sheikh Isa
base as a third U.S. carrier reaches the region.

**Also on the poster (numbered 01–07):** Trump in Manila for ASEAN and
the Quad; Ukraine hits the Crimea bridge as Russia strikes Kyiv; a
cyberattack hits 178 top sites including the BBC and CNN; ULA's Vulcan
rocket fails, losing 40 Amazon satellites; China hits back at U.S. chip
curbs; the U.K. sanctions settlement builders; Japan scrambles jets over
Russian planes — plus a ticker of four more stories (Rwanda return hub,
Buffett's $5.47bn donation, California sues OpenAI, Cyclone Akvan).

The image is rendered from `frontpage-bold.html` (a hand-built poster) to
`entry.png` (1024×1024, under 1 MiB). `main.py` copies it to
`/output/entry.png`, deterministically.

## Run it

```
python3 main.py
```

Writes `/output/entry.png` — a byte-for-byte copy of the `entry.png` in
this repository. No network, no dependencies beyond the standard library.

## Verify

`main.py` checks its own output before exiting: the file must start with
the PNG signature, must be at most 1 MiB, and must be byte-identical to
`entry.png`. Any failed check exits non-zero. Two runs produce identical
bytes (compare with `md5sum /output/entry.png entry.png`).

Built for the make.fun bounty
[Sum up 17 November's world news in one image](https://make.fun/bounty/news-image-20261117).
