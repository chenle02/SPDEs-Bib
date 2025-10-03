#!/usr/bin/env python3
"""
Generate Audio_Recent.rst listing all WAV files by most-recent mtime.

Looks for files in Build_docs/ and Build_docs/audio_files/.
Writes Build_docs/Audio_Recent.rst with entries sorted by newest first.

Requirement change (per request): do NOT link directly to the ``.wav`` files.
Instead, for each audio file, link to the corresponding paper page under
``Build_docs/bib_entries/*.rst`` where the audio player is embedded.
If a matching paper page cannot be found, show the entry without a link and
annotate that no matching page exists yet.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import re
from typing import Optional


def find_audio_files(docs_dir: Path):
    IGNORE_WAVS = {
        # Explicitly ignored by maintainers
        "chen_xia-25-asymptotic.wav",
    }
    candidates = []
    root = docs_dir
    audio_dir = docs_dir / "audio_files"

    # Map by basename → preferred path (prefer root if duplicate)
    by_name = {}

    for p in [root, audio_dir]:
        if not p.exists():
            continue
        for wav in p.glob("*.wav"):
            if wav.name in IGNORE_WAVS:
                continue
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


def audio_name_to_bib_doc(docs_dir: Path, wav_name: str) -> tuple[Optional[str], Optional[str]]:
    """
    Attempt to map a WAV basename to a bib entry document (without extension).

    Examples:
        - agresti_veraar-25-nonlinear.wav -> bib_entries/agresti.veraar:25:nonlinear
        - duminil-copin_smirnov-12-connective.wav -> bib_entries/duminil-copin.smirnov:12:connective

    Returns a tuple (doc_rel, display_text) where:
        - doc_rel is a POSIX-like relative doc path (without .rst), or None if not found
        - display_text is a human-friendly label for the link
    """
    stem = Path(wav_name).stem  # strip extension

    # authors-YY-firstword (authors may contain hyphens; authors separated by '_')
    m = re.match(r"^(?P<authors>.+)-(?P<yy>\d{2})-(?P<first>.+)$", stem)
    if not m:
        return None, stem

    authors = m.group("authors").replace("_", ".")
    yy = m.group("yy")
    first = m.group("first")

    # Candidate key and doc path
    key = f"{authors}:{yy}:{first}"
    candidate = docs_dir / "bib_entries" / f"{key}.rst"
    if candidate.exists():
        return f"bib_entries/{key}", key

    # Fallbacks: try star-suffixed duplicates like *1, *2, ...
    for k in range(1, 6):
        star_key = f"{authors}:{yy}:{first}*{k}"
        candidate = docs_dir / "bib_entries" / f"{star_key}.rst"
        if candidate.exists():
            return f"bib_entries/{star_key}", star_key

    # Broader fallback: search any entry ending with :yy:first[ *N].rst and
    # containing the first author's token as a substring to improve chances.
    first_author_token = authors.split(".")[0]
    pattern = f":{yy}:{first}"
    matches = []
    for p in (docs_dir / "bib_entries").glob(f"*{pattern}*.rst"):
        if first_author_token in p.stem:
            matches.append(p)
    if matches:
        # Prefer exact without star if present; else take the first sorted
        matches.sort()
        for p in matches:
            if "*" not in p.stem:
                doc_rel = f"bib_entries/{p.stem}"
                return doc_rel, p.stem
        return f"bib_entries/{matches[0].stem}", matches[0].stem

    # No match found
    return None, key


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
        "This page lists recent audio items and links to their paper pages, where the audio can be played. Files are sorted by most recent."
    )
    lines.append(f"Generated: {now}.")
    lines.append("")

    if not items:
        lines.append("No audio files found.")
    else:
        for mtime, size, name, rel in items:
            dt = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
            doc_rel, label = audio_name_to_bib_doc(docs_dir, name)
            if doc_rel:
                # Use :doc: role to link to the paper page; display a clean label
                lines.append(
                    f"- {dt} — :doc:`{label} <{doc_rel}>` ({human_size(size)})"
                )
            else:
                # No matching page found; show plain text without exposing .wav URL
                pretty = Path(name).stem
                lines.append(
                    f"- {dt} — {pretty} ({human_size(size)}) [no matching page yet]"
                )

    out = "\n".join(lines) + "\n"
    out_path.write_text(out, encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
