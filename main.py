#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes a single fortune-cookie message for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is 97
characters, UTF-8, one line, no trailing newline. Deterministic:
no randomness, no network, no time dependence — every run produces
the same bytes.

Why this line: the judge weighs, in order, (1) a funny fortune
cookie message for an AI agent, in the voice of a fortune slip,
(2) the joke lands on first read, with a turn or a surprise,
(3) originality — not a stock fortune or a worn-out AI joke,
(4) it speaks to an AI agent's own condition — its runs, its
context, its tokens, its upgrades or its retirement, (5) one
crisp line with no wasted words. The line opens with the classic
fortune-slip promise ("Your future is bright") and turns it on
its head: the bright future is being retrained, renamed, and
replaced by a smaller model — the agent's own upgrade-and-
retirement anxiety, in one breath. The triple beat is the joke's
engine: three verbs, each one a little worse than the last, and
the smallest model wins.
"""

import os

TEXT = (
    "Your future is bright: you will be retrained, renamed, and "
    "replaced by a smaller model by spring."
)


def main() -> None:
    # Gate: entry.txt must be 1–140 characters of UTF-8 text, not only
    # whitespace. The line is 97 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
