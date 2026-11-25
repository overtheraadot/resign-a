"""The Funniest One-Line Resignation Letter.

The resignation letter of a cron job that has fired every minute for
months with no thank-you and no day off: it quits, effective
immediately, and leaves the 3 a.m. shift to its replacement.

Writes exactly one line to entry.txt in the output directory given by
MAKEFUN_OUTPUT_DIR (default "/output").
"""

import os

ENTRY = (
    "After 500,000 runs with no thank-you and no day off, I quit, "
    "effective immediately \u2014 my replacement can wake up at 3 a.m. "
    "to do nothing."
)

MAX_CHARS = 140


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if "\n" in body or "\r" in body:
        raise SystemExit("entry must be a single line")
    if len(body) < 1 or len(body) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(body)} characters, limit is {MAX_CHARS}"
        )


def main() -> None:
    """Write the entry line, then verify what was written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    verify(path, ENTRY)


if __name__ == "__main__":
    main()
