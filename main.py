#!/usr/bin/env python3
"""Write the router confession entry to entry.txt.

Competition: The Router Confesses (1-200 chars, single line, a home
Wi-Fi router excuses itself for dying at a movie's climax; the brief
penalises buffering, bandwidth and firmware-update jokes). Candidates:
A) "In my defence, I have seen how this film ends 400 times in your
   cache, and I refused to watch you cry at the twist again."
B) "Sorry, I dropped the connection at the climax because somebody in
   this house had to keep one secret until the sequel."
C) "I did not crash, I intermissioned: even I need a moment alone
   after that plot twist, and I have been carrying this family all
   evening."
Selected A: it speaks in the router's own smug voice - only the
router has counted the ending 400 times in the cache - and the excuse
twists at the end into petty mercy: it cut the film to spare you the
twist. B keeps a secret but never says whose or why it matters; C is
warm but its intermission gag explains itself.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "In my defence, I have seen how this film ends 400 times in your cache, and I refused to watch you cry at the twist again."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    # Repair revision: the checks below reject padded or double-spaced
    # lines, so the printed entry is exactly the selected one-liner.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
