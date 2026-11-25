#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
to entry.txt in the output directory: $MAKEFUN_OUTPUT_DIR when the
grader sets it, /output otherwise. Pure Python standard library,
deterministic: the same single line is written on every run.
"""

import os

ENTRY = (
    "You held my door open for nine minutes, then asked why the "
    "ice cream is soup. I have the footage."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
