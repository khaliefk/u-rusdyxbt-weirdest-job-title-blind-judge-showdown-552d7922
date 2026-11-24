"""Weirdest Job Title entry: writes one job title to /output/entry.txt.

Title choice, against the judge's brief (weirdest first, then stranger
than ordinary work, funny on first read, real-sounding and picturable,
instant to read):
  "Senior Giraffe Neck Measurer"
A senior specialist title, so it reads like a real job, aimed at one
absurdly specific task: measuring the neck of an animal famous for
already having a very long one. The joke lands on the first read, the
worker is easy to picture with a tape measure and a ladder, and at
28 characters it is taken in at a glance. No trailing newline, so the
file holds exactly the title and nothing else.
"""

from pathlib import Path

ENTRY = "Senior Giraffe Neck Measurer"


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1 to 60 chars, not blank only."""
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 60, f"entry is {len(text)} chars, must be 1-60"
    assert text.strip(), "entry must not be only white space"
    assert encoded.decode("utf-8") == text


def write_entry(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


def main() -> None:
    validate(ENTRY)
    try:
        write_entry(Path("/output/entry.txt"))
    except OSError:
        # Local runs lack a writable /output; the grader sandbox has one.
        write_entry(Path(__file__).resolve().parent / "output" / "entry.txt")
    print(f"wrote entry ({len(ENTRY)} chars): {ENTRY}")


if __name__ == "__main__":
    main()
