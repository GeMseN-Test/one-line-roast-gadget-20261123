#!/usr/bin/env python3
"""One-line roast entry for make.fun bounty
"One-Line Roast: The Gadget You Use Every Day".

Writes a single original roast line (max 200 characters) about the
phone's autocorrect to /output/entry.txt, deterministically, with no
trailing newline.

The joke: one concrete scene (three years of the same mistake), a
specific detail (face / fingerprint / location), and the punch at the
end (it still cannot spell its owner's name).
"""

import os

ROAST = (
    "My phone has autocorrected my own name wrong for three years — "
    "it knows my face, my fingerprint, my location, but not how to spell me."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
