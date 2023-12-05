#!/usr/bin/env python3
#
# By Le Chen and Chatgpt
# chenle02@gmail.com / le.chen@auburn.edu
# Created at Mon Dec  4 08:12:34 PM EST 2023
#

import bibtexparser
import os

# Load BibTeX file
with open("../All.bib") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Create a directory for individual entries
os.makedirs("bib_entries", exist_ok=True)

# Generate RST files
for entry in bib_database.entries:
    cite_key = entry["ID"]
    with open(f"bib_entries/{cite_key}.rst", "w") as file:
        file.write(f"{cite_key}\n")
        file.write("=" * len(cite_key) + "\n\n")

        # Add a citation for the entry
        file.write(f".. :cite:t:`{cite_key}`\n\n")

        # Add bibliography directive
        file.write(".. bibliography:: ../../All-test.bib\n\n")

        # Write the BibTeX source code
        file.write("**BibTeX Entry:**\n\n")
        file.write(".. code-block:: bibtex\n\n")
        file.write(f'   @{entry["ENTRYTYPE"]}{{{cite_key},\n')
        for key, value in entry.items():
            if key != "ENTRYTYPE":
                file.write(f"   {key} = {{{value}}},\n")
        file.write("   }\n")
        file.write("\n`Back to index <../index>`_\n")
