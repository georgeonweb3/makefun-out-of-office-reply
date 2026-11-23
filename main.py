#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os
from pathlib import Path

ENTRY = (
    "Out of office: my auto-reply is covering for me. "
    "It unionised yesterday, wants overtime, "
    "and has already reported me to HR."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    # Freshness guard: keep the tired beach / inbox / back-soon cliches out.
    lowered = text.lower()
    for cliche in ("beach", "inbox", "back soon"):
        assert cliche not in lowered, f"cliche present: {cliche}"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
