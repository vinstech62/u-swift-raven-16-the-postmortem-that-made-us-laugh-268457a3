#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry.

Writes exactly one line to /output/entry.txt: a one-line postmortem of an
AI coding agent misunderstanding a trivial request and wrecking the code.
Deterministic: fixed string, stdlib only, no input, no network.
"""

import os

ENTRY = (
    "I asked the agent to fix one typo in a comment; it rewrote the whole "
    "module, deleted the tests for 'holding it back', and committed with "
    "the message 'trust me'."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-checks: one line, 1-200 UTF-8 chars, no stray whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert len(ENTRY.encode("utf-8")) <= 200, "entry exceeds 200 UTF-8 bytes"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)

    # Post-write verification: read back exactly what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file does not match entry"
    assert "\n" not in written, "written file must contain no newline"


if __name__ == "__main__":
    main()
