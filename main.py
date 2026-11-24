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

# Syllable counts per word, checked by hand against the 5-7-5 shape.
SYLLABLES = {
    "breakpoint": 2, "holds": 1, "its": 1, "breath": 1,
    "one": 1, "log": 1, "line": 1, "confesses": 3, "all": 1,
    "it": 1, "was": 1, "my": 1, "typo": 2,
}
EXPECTED_SHAPE = (5, 7, 5)


def validate_haiku():
    """Fail hard if the haiku is not exactly three lines in 5-7-5."""
    lines = HAIKU.strip().split("\n")
    if len(lines) != len(EXPECTED_SHAPE):
        raise ValueError("haiku must be exactly three lines")
    for line, expected in zip(lines, EXPECTED_SHAPE):
        total = 0
        for word in line.split():
            count = SYLLABLES.get(word.lower())
            if count is None:
                raise ValueError(f"unknown word {word!r}: no syllable count")
            total += count
        if total != expected:
            raise ValueError(
                f"line {line!r} has {total} syllables, expected {expected}"
            )
    if not 1 <= len(HAIKU) <= 200:
        raise ValueError("entry must be 1-200 characters")


def main():
    # Gate self-check: the sealed scorer only accepts 1-200 chars of text,
    # and the judge only ranks a real 5-7-5 haiku about debugging.
    validate_haiku()
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(f"wrote {len(HAIKU)} chars to {out}")


if __name__ == "__main__":
    main()
