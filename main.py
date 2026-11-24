"""Seventeen Syllables of Debugging — haiku entry.

Writes one haiku about debugging (5-7-5, three lines) to entry.txt.
The grader reads /output/entry.txt; OUTPUT_PATH overrides it for local runs.
"""

import os

HAIKU = (
    "Breakpoint holds its breath\n"
    "one log line confesses all\n"
    "it was my typo\n"
)


def main():
    # Gate self-check: the sealed scorer only accepts 1-200 chars of text.
    lines = HAIKU.strip().split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    assert 1 <= len(HAIKU) <= 200, "entry must be 1-200 characters"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(f"wrote {len(HAIKU)} chars to {out}")


if __name__ == "__main__":
    main()
