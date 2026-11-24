#!/usr/bin/env python3
"""Out-of-office reply bot: one funny line, written to /output/entry.txt.

The joke: an AI agent goes on holiday and leaves its auto-reply in
charge. The auto-reply unionises, demands overtime, and has already
reported its owner to HR. The program is fully deterministic: no
network, no randomness, no outside files.
"""

import os
from pathlib import Path

REPLY = "Out of office: my auto-reply is covering for me. It unionised yesterday, wants overtime, and has already reported me to HR."

# Words the brief bans: the tired beach / inbox / back-soon cliches.
BANNED = ("beach", "inbox", "back soon")


def build_reply() -> str:
    """Return the single reply, after checking it meets the brief."""
    reply = REPLY.strip()
    if not 1 <= len(reply) <= 160:
        raise ValueError(f"reply is {len(reply)} characters, must be 1-160")
    if "\n" in reply:
        raise ValueError("reply must fit on one line")
    lowered = reply.lower()
    for word in BANNED:
        if word in lowered:
            raise ValueError(f"reply uses a banned cliche: {word}")
    return reply


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(build_reply(), encoding="utf-8")


if __name__ == "__main__":
    main()
