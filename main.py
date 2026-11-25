#!/usr/bin/env python3
"""Write the GPS's one-line excuse to /output/entry.txt.

The entry is a single line of plain text, at most 200 characters, in the
GPS's own smug, defensive voice: it insists the cul-de-sac was a shortcut
and blames the map for leaving out the wedding in the middle and the lake
at the end. Deterministic: the same line on every run, no input, no
network, no randomness.
"""

import hashlib
import os
import sys
import unicodedata

ENTRY = "Relax, that cul-de-sac was a shortcut \u2014 the map just left out the wedding in the middle and the lake at the end."

OUTPUT_PATH = "/output/entry.txt"


def gate(line: str) -> None:
    """Fail loudly unless the line passes the competition gate."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(unicodedata.category(ch) == "Cc" for ch in line):
        raise ValueError("entry must not contain control characters")
    encoded = line.encode("utf-8")  # raises if not valid UTF-8 text
    if len(encoded) > 200:
        raise ValueError(f"entry is {len(encoded)} bytes, over the 200-byte cap")


def main() -> int:
    gate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Post-write re-read: the file on disk must be byte-identical to the
    # gated line, with no trailing newline added.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("written entry does not match the gated line")
    print(f"wrote {len(written)} bytes to {OUTPUT_PATH}")
    print(f"md5: {hashlib.md5(written).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
