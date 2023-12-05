#!/usr/bin/env python3
#
# By Le Chen and Chatgpt
# chenle02@gmail.com / le.chen@auburn.edu
# Created at Mon Dec  4 08:12:34 PM EST 2023
#

import bibtexparser
import os

bib_file_name = "../All-test.bib"
parent_rst_name = "Reference.rst"

# Load BibTeX file
with open(bib_file_name) as bibtex_file:
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

        # Write the BibTeX source code
        file.write("**BibTeX Entry:**\n\n")
        file.write(".. code-block:: bibtex\n\n")
        file.write(f'   @{entry["ENTRYTYPE"]}{{{cite_key},\n')
        for key, value in entry.items():
            if key != "ENTRYTYPE":
                file.write(f"   {key} = {{{value}}},\n")
        file.write("   }\n\n")

        # Add bibliography directive
        file.write(f".. bibliography:: ../{bib_file_name}\n\n")
        file.write(f"\n`Back to index <../{parent_rst_name}>`_\n")

# Create or open the index file
with open(parent_rst_name, "w") as index_file:
    # Write the header for the index file
    index_file.write("Welcome to the SPDEs-Bib Index\n")
    index_file.write("=================================\n\n")

    # Add an introductory line or description if needed
    index_file.write("Here is a list of all entries in the SPDEs-Bib database:\n\n")

    # Create links to each entry's page
    for entry in bib_database.entries:
        cite_key = entry["ID"]
        index_file.write(f"- `{cite_key} <bib_entries/{cite_key}.html>`_\n")
