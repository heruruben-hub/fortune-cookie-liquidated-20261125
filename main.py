#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun bounty entry.

Writes one fortune cookie line to /output/entry.txt. The line is for a
crypto trader who was just liquidated, reading a fortune at 3am: fortune
voice, the joke lands on the loss, rueful and warm, never cruel or smug.
"""

import os

FORTUNE = "The market took your coins, not your luck: great fortunes begin the day you stop chasing the last one."


def main() -> None:
    # Gate check: 1-160 characters, at most 20 words, not only whitespace.
    assert 1 <= len(FORTUNE) <= 160, "fortune must be 1-160 characters"
    assert len(FORTUNE.split()) <= 20, "fortune must be at most 20 words"
    assert FORTUNE.strip(), "fortune must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
