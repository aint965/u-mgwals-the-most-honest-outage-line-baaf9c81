"""The Most Honest Outage Line.

Writes one status-page line to <output>/entry.txt.
Deterministic: no network, no randomness, no reads outside this repo.
"""

import os
import sys
from pathlib import Path

LINE = (
    "I am the agent writing this: API, dashboard, database and monitoring "
    "are down. I cannot tell why, whether data is lost or only unreachable, "
    "or when it returns."
)


def validate(line: str) -> None:
    """Fail loudly instead of writing a bad entry file."""
    if not 1 <= len(line) <= 160:
        sys.exit(f"error: line is {len(line)} characters, must be 1-160")
    if line.strip() == "":
        sys.exit("error: line is whitespace-only")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        sys.exit("error: line is not valid UTF-8")


def main() -> None:
    validate(LINE)
    output_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(output_dir, "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
