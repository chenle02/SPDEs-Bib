#!/usr/bin/env python3
#
# By Le Chen and ChatGPT (patched)
# This version enables common_strings to support month macros like 'jan', 'mar', etc.

import os
import glob
import subprocess
import argparse

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser


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
with open(bib_file_name) as bibtex_file:
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
with open(parent_rst_name, "w") as parent_rst:
    parent_rst.write("Here is a list of all entries in the SPDEs-Bib database:\n\n")
    parent_rst.write("References listed by cite keys\n")
    parent_rst.write("=" * len("References listed by cite keys") + "\n\n")

    sorted_entries = sorted(bib_database.entries, key=lambda x: x["ID"].upper())

    current_letter = ""
    for entry in sorted_entries:
        count += 1
        cite_key = entry["ID"]
        print(f"Processing {count}/{len(bib_database.entries)}: {cite_key}")

        first_letter = cite_key[0].upper()
        if first_letter != current_letter:
            current_letter = first_letter
            parent_rst.write(f"\n{current_letter}\n")
            parent_rst.write("-" * len(current_letter) + "\n\n")

        bib_entry_filename = f"bib_files/{cite_key}.bib"

        if args.fast and os.path.exists(bib_entry_filename):
            pass
        else:
            with open(bib_entry_filename, "w") as bibfile:
                db = bibtexparser.bibdatabase.BibDatabase()
                db.entries = [entry]
                bibfile.write(writer.write(db))
            if not args.fast:
                subprocess.run(
                    ["bibtex-tidy", bib_entry_filename, "-m"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

        rst_entry_filename = f"bib_entries/{cite_key}.rst"
        with open(rst_entry_filename, "w") as file:
            file.write(f"{cite_key}\n")
            file.write("=" * len(cite_key) + "\n\n")
            file.write(f":cite:t:`{cite_key}`\n\n")
            file.write("**BibTeX Entry:**\n\n")
            file.write(".. code-block:: bibtex\n\n")

            # Write raw BibTeX entry
            with open(bib_entry_filename, "r") as bibfile:
                for line in bibfile:
                    file.write(f"   {line}")

            # Append clickable link if entry has a URL field
            url = entry.get("url")
            if url:
                url = url.strip().strip("{} ,")
                file.write(f"\n`The URL link to the source <{url}>`__\n\n")

            file.write(f"\n`Back to index <../{parent_rst_html}>`__\n")

        parent_rst.write(
            f"- :cite:t:`{cite_key}` : `{cite_key} <bib_entries/{cite_key}.html>`_\n"
        )
