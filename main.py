#!/usr/bin/env python3
"""One Word From Grandma.

Writes the single word our grandma would text about AI to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``) and prints it.
Stdlib only, deterministic, no input, no network.
"""

import os

# The word: "artifishal".
#
# Grandma spells by ear. "Artificial" is pronounced art-uh-FISH-uhl, so
# when she texts about artificial intelligence she writes what she hears:
# artifishal. It is the typo she would actually make (the brief counts
# those), it names the A of AI itself, and the fish in the middle makes
# the joke land with no caption at all. Warm, a little baffled, and not
# the obvious "robot" every other entry reaches for.
WORD = "artifishal"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
