#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes exactly one sentence (at most 280 characters) to /output/entry.txt.
Python standard library only -- the grader image has no third-party packages.
"""

import os

# PART_A: the entry -- one childhood memory, written fresh for this bounty.
# Concrete mechanism (ladling rice from a chipped blue pot) + specific
# numbers (Sunday at six, thirty years later) + everyday trigger scene
# (smell of steam on a cold evening) + warm-ache closer (waiting for the
# first spoonful on a stool in grandmother's kitchen).
SENTENCE = (
    "Every Sunday at six my grandmother ladled rice from the same chipped "
    "blue pot, and thirty years later the smell of steam on a cold evening "
    "still sends me straight back to her kitchen, standing on a stool, "
    "waiting for the first spoonful."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


# PART_B: self-check guard -- the gate's own terms, enforced before exit.
def _validate(text: str) -> None:
    assert 1 <= len(text) <= 280, f"length {len(text)} out of range 1-280"
    assert text.strip() == text and text.strip(), "must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), (
        "must be exactly one sentence"
    )


if __name__ == "__main__":
    _validate(SENTENCE)
    raise SystemExit(main())
