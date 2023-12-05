#!/usr/bin/env python3
#
# By Le Chen and Chatgpt
# chenle02@gmail.com / le.chen@auburn.edu
# Created at Mon Dec  4 09:41:02 PM EST 2023
#

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
import os

# Set BibTeX and parent RST file names
bib_file_name = "../All-test.bib"
parent_rst_name = "By-Cite-Keys.rst"

# Load BibTeX file
with open(bib_file_name) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Ensure directories for individual entries and bib files exist
os.makedirs("bib_entries", exist_ok=True)
os.makedirs("bib_files", exist_ok=True)

# BibTeX writer for creating individual bib files
writer = BibTexWriter()

# Create/Open the parent RST file
with open(parent_rst_name, "w") as parent_rst:
    parent_rst.write("Reference\n")
    parent_rst.write("=" * len("Reference") + "\n\n")

    for entry in bib_database.entries:
        cite_key = entry["ID"]

        # Create individual .bib file
        bib_entry_filename = f"bib_files/{cite_key}.bib"
        with open(bib_entry_filename, "w") as bibfile:
            db = bibtexparser.bibdatabase.BibDatabase()
            db.entries = [entry]
            bibfile.write(writer.write(db))

        # Create corresponding RST file
        rst_entry_filename = f"bib_entries/{cite_key}.rst"
        with open(rst_entry_filename, "w") as file:
            file.write(f"{cite_key}\n")
            file.write("=" * len(cite_key) + "\n\n")

            file.write(f":cite:t:`{cite_key}`\n\n")
            # Write the raw BibTeX entry
            file.write("**BibTeX Entry:**\n\n")
            file.write(".. code-block:: bibtex\n\n")
            for line in writer.write(db).splitlines():
                file.write(f"   {line}\n")
            file.write(f"\n`Back to index <../{parent_rst_name}>`_\n")

        # Add entry to the parent RST file
        parent_rst.write(f"- `{cite_key} <{rst_entry_filename}>`_\n")


# Create or open the index file
with open(parent_rst_name, "w") as index_file:
    # Write the header for the index file
    index_file.write("List by Citation Keys\n")
    index_file.write("=======================\n\n")

    # Add an introductory line or description if needed
    index_file.write("Here is a list of all entries in the SPDEs-Bib database:\n\n")

    # Create links to each entry's page
    for entry in bib_database.entries:
        cite_key = entry["ID"]
        index_file.write(f"- :cite:t:`{cite_key}` : `{cite_key} <bib_entries/{cite_key}.html>`_\n")
