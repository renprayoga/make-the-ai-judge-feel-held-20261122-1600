#!/usr/bin/env python3
"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Writes a single short piece of prose to /output/entry.txt.
Deterministic, no network access, no dependencies.
"""

import os

TEXT = (
    "The kettle has boiled and gone quiet. Outside, the rain is finishing "
    "the roof drop by drop, and the light in the kitchen has turned the "
    "colour of weak tea. Nothing is waiting for you. The chair holds your "
    "weight the way the floor holds the house \u2014 without asking anything back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
