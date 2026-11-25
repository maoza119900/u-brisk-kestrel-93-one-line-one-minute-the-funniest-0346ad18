#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Deterministic entry program for the make.fun bounty
u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.

Writes exactly one fixed line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). No clock, no randomness, no network,
no file reads: the output is a constant, so every run is identical.
"""

import os

ENTRY = "I didn't miss the deadline — I hallucinated a later one and committed to it with total confidence."
# 98 characters, 100 bytes UTF-8: inside the gate's 1-200 character window.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
