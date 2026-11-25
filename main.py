#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes a single sentence that could have replaced an entire pointless
meeting to /output/entry.txt (or to the path in ENTRY_OUTPUT when set,
so the program can be exercised locally without the grader mount).

The line: a meeting with no decision, no owner and no end has nothing
left to justify it -- it is only a calendar invite with witnesses.
"""

import os
import sys

ENTRY = (
    "This meeting has no decision, no owner, and no end "
    "\u2014 just a calendar invite with witnesses."
)

# One sentence, one line, no context needed: the meeting is indicted
# by its own missing parts (decision, owner, end) and the punchline
# reframes the attendees as witnesses to a non-event.


def main() -> int:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print("entry text out of bounds", file=sys.stderr)
        return 1
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
