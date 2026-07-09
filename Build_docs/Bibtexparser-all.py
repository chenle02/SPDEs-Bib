#!/usr/bin/env python3
#
# By Le Chen and ChatGPT (patched)
# This version enables common_strings to support month macros like 'jan', 'mar', etc.

import os
import glob
import hashlib
import subprocess
import argparse

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser


def file_content_hash(path):
    """Return SHA-256 hex digest of a file, or None if it doesn't exist."""
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        return None


def write_if_changed(path, content):
    """Write content to path only if it differs from existing file.
    Returns True if written (new/changed), False if skipped (identical)."""
    content_bytes = content.encode("utf-8")
    new_hash = hashlib.sha256(content_bytes).hexdigest()
    if file_content_hash(path) == new_hash:
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


# Set up argument parser
parser = argparse.ArgumentParser(description="Fast processing.")
parser.add_argument("--fast", action="store_true", help="Run the script in fast mode")
args = parser.parse_args()

# Set BibTeX and parent RST file names
bib_file_name = "../All.bib"
parent_rst_name = "By-Cite-Keys.rst"
parent_rst_html = os.path.splitext(parent_rst_name)[0] + ".html"

# Load BibTeX file with parser that understands common month/name strings
print(f"\nLoading {bib_file_name}...")
with open(bib_file_name, errors="replace") as bibtex_file:
    parser = BibTexParser(common_strings=True)
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

os.makedirs("bib_entries", exist_ok=True)
os.makedirs("bib_files", exist_ok=True)
if not args.fast:
    for directory in ("bib_entries", "bib_files"):
        for f in glob.glob(os.path.join(directory, "*")):
            os.remove(f)

# BibTeX writer for creating individual bib files
writer = BibTexWriter()

print(f"\nWorking on {len(bib_database.entries)} entries...")
count = 0
stats = {"bib_written": 0, "bib_skipped": 0, "rst_written": 0, "rst_skipped": 0}

# Track current entry keys for orphan cleanup
current_keys = set()

with open(parent_rst_name, "w") as parent_rst:
    parent_rst.write("Here is a list of all entries in the SPDEs-Bib database:\n\n")
    parent_rst.write("References listed by cite keys\n")
    parent_rst.write("=" * len("References listed by cite keys") + "\n\n")

    sorted_entries = sorted(bib_database.entries, key=lambda x: x["ID"].upper())

    current_letter = ""
    for entry in sorted_entries:
        count += 1
        cite_key = entry["ID"]
        current_keys.add(cite_key)

        first_letter = cite_key[0].upper()
        if first_letter != current_letter:
            current_letter = first_letter
            parent_rst.write(f"\n{current_letter}\n")
            parent_rst.write("-" * len(current_letter) + "\n\n")

        bib_entry_filename = f"bib_files/{cite_key}.bib"

        if args.fast and os.path.exists(bib_entry_filename):
            stats["bib_skipped"] += 1
        else:
            db = bibtexparser.bibdatabase.BibDatabase()
            db.entries = [entry]
            bib_content = writer.write(db)
            if write_if_changed(bib_entry_filename, bib_content):
                stats["bib_written"] += 1
            else:
                stats["bib_skipped"] += 1
            if not args.fast:
                subprocess.run(
                    ["bibtex-tidy", bib_entry_filename, "-m"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

        # Build RST content in memory first, then write only if changed
        rst_lines = []
        rst_lines.append(f"{cite_key}\n")
        rst_lines.append("=" * len(cite_key) + "\n\n")
        rst_lines.append(f":cite:t:`{cite_key}`\n\n")
        rst_lines.append("**BibTeX Entry:**\n\n")
        rst_lines.append(".. code-block:: bibtex\n\n")

        # Read raw BibTeX entry
        with open(bib_entry_filename, "r") as bibfile:
            for line in bibfile:
                rst_lines.append(f"   {line}")

        # Append clickable link if entry has a URL field
        url = entry.get("url")
        if url:
            url = url.strip().strip("{} ,")
            # URL-encode < and > characters to prevent RST hyperlink parsing issues
            url = url.replace("<", "%3C").replace(">", "%3E")
            rst_lines.append(f"\n`The URL link to the source <{url}>`__\n\n")

        rst_lines.append(f"\n`Back to index <../{parent_rst_html}>`__\n")
        rst_content = "".join(rst_lines)

        rst_entry_filename = f"bib_entries/{cite_key}.rst"
        if write_if_changed(rst_entry_filename, rst_content):
            stats["rst_written"] += 1
        else:
            stats["rst_skipped"] += 1

        # Progress: only print every 500 entries or at the end
        if count % 500 == 0 or count == len(bib_database.entries):
            print(f"  Progress: {count}/{len(bib_database.entries)}")

        parent_rst.write(
            f"- :cite:t:`{cite_key}` : `{cite_key} <bib_entries/{cite_key}.html>`_\n"
        )

# --- Orphan cleanup (fast and non-fast) ---
orphans_removed = 0
for directory, ext in [("bib_entries", ".rst"), ("bib_files", ".bib")]:
    for filepath in glob.glob(os.path.join(directory, f"*{ext}")):
        basename = os.path.splitext(os.path.basename(filepath))[0]
        if basename not in current_keys:
            os.remove(filepath)
            orphans_removed += 1

# --- Summary ---
print(f"\nDone: {len(bib_database.entries)} entries processed.")
print(f"  Bib files:  {stats['bib_written']} written, {stats['bib_skipped']} skipped")
print(f"  RST files:  {stats['rst_written']} written, {stats['rst_skipped']} skipped")
if orphans_removed > 0:
    print(f"  Orphans:    {orphans_removed} stale files removed")
