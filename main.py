#!/usr/bin/env python3
"""Last Text at One Percent — entry program.

Writes the phone's final text message to /output/entry.txt.
Python 3.13 stdlib only, no network, deterministic output.
"""

import os

# The phone's last words: a confession, a grievance, and a punchline
# that only a dying phone could deliver. The twist: the 47 unread tabs
# outlive the phone itself — the thing it kept open dies last.
# The closing lands as a three-beat list of phone-specific miseries:
# buffering, overheating, ignored — the phone's whole life in three words.
ENTRY = (
    "1% left. The 47 open tabs outlived me, and I never read a single one. "
    "I die as I lived: buffering, overheating, ignored."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
