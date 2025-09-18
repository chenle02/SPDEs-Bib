#!/usr/bin/env python3
"""
Generate Audio_Recent.rst listing all WAV files by most-recent mtime.

Looks for files in Build_docs/ and Build_docs/audio_files/.
Writes Build_docs/Audio_Recent.rst with links sorted by newest first.
"""

import os
import sys
from datetime import datetime
from pathlib import Path


def find_audio_files(docs_dir: Path):
    candidates = []
    root = docs_dir
    audio_dir = docs_dir / "audio_files"

    # Map by basename → preferred path (prefer root if duplicate)
    by_name = {}

    for p in [root, audio_dir]:
        if not p.exists():
            continue
        for wav in p.glob("*.wav"):
            key = wav.name
            # Prefer root if already seen from audio_dir
            if key in by_name and by_name[key].parent == root:
                continue
            by_name[key] = wav

    for name, path in by_name.items():
        try:
            mtime = path.stat().st_mtime
            size = path.stat().st_size
        except OSError:
            continue
        rel = path.relative_to(docs_dir)
        candidates.append((mtime, size, name, rel))

    # Newest first
    candidates.sort(key=lambda t: t[0], reverse=True)
    return candidates


def human_size(nbytes: int) -> str:
    # Simple MB representation
    return f"{nbytes / (1024*1024):.1f} MB"


def main(argv=None) -> int:
    docs_dir = Path(__file__).resolve().parent
    out_path = docs_dir / "Audio_Recent.rst"

    items = find_audio_files(docs_dir)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = []
    title = "Recent Audio Files"
    lines.append(title)
    lines.append("=" * len(title))
    lines.append("")
    lines.append(
        "This page lists all available audio files sorted by the time they were added."
    )
    lines.append(f"Generated: {now}.")
    lines.append("")

    if not items:
        lines.append("No audio files found.")
    else:
        for mtime, size, name, rel in items:
            dt = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
            lines.append(
                f"- {dt} — `{name} <{rel.as_posix()}>`__ ({human_size(size)})"
            )

    out = "\n".join(lines) + "\n"
    out_path.write_text(out, encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

