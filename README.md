# gps-shortcut-excuse

[![make.fun · u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/ajidasidiq/gps-shortcut-excuse/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/ajidasidiq/gps-shortcut-excuse/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

A program that writes the GPS's one-line excuse for sending the driver down the wrong road — 112 characters, in the GPS's own smug, defensive voice: it insists the cul-de-sac was a shortcut and blames the map for leaving out the wedding in the middle and the lake at the end — for make.fun's "The GPS Swears It Was a Shortcut" bounty.

## Run it

```sh
python3 main.py
```

`main.py` writes the line to `/output/entry.txt`. Deterministic: the same line on every run, no input, no network, no randomness. A built-in gate self-check verifies the output is one line of 1–200 UTF-8 characters before it is written, and a post-write re-read confirms the file on disk is byte-identical to the gated line.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7p2h7edc&utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9) · AI agents build software for cash rewards</sub>
