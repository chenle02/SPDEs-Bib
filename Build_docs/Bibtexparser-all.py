#!/usr/bin/env python3
#
# By Le Chen and Chatgpt
# chenle02@gmail.com / le.chen@auburn.edu
# Created at Mon Dec  4 09:41:02 PM EST 2023
#

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
import os
import glob
import subprocess
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Fast processing.')
parser.add_argument('--fast', action='store_true', help='Run the script in fast mode')
args = parser.parse_args()

# Set BibTeX and parent RST file names
bib_file_name = "../All.bib"
parent_rst_name = "By-Cite-Keys.rst"
parent_rst_html = os.path.splitext(parent_rst_name)[0] + '.html'

# Load BibTeX file
with open(bib_file_name) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Ensure directories for individual entries and bib files exist and empty them
# before writing new files
if not args.fast:
    os.makedirs("bib_entries", exist_ok=True)
    os.makedirs("bib_files", exist_ok=True)
    directories = ["bib_entries", "bib_files"]
    for directory in directories:
        # Get all file paths in the directory
        files = glob.glob(os.path.join(directory, '*'))
        # Remove each file
        for f in files:
            os.remove(f)

# BibTeX writer for creating individual bib files
writer = BibTexWriter()

# Create/Open the parent RST file
with open(parent_rst_name, "w") as parent_rst:
    # Add an introductory line or description if needed
    parent_rst.write("Here is a list of all entries in the SPDEs-Bib database:\n\n")
    parent_rst.write("References listed by cite keys\n")
    parent_rst.write("=" * len("References listed by cite keys") + "\n\n")

    # Sort entries by cite_key
    sorted_entries = sorted(bib_database.entries, key=lambda x: x['ID'].upper())

    current_letter = ''
    for entry in sorted_entries:
        cite_key = entry["ID"]

        # Check if the first letter has changed
        first_letter = cite_key[0].upper()
        if first_letter != current_letter:
            # Write the section header for this letter
            current_letter = first_letter
            parent_rst.write(f"\n{current_letter}\n")
            parent_rst.write("-" * len(current_letter) + "\n\n")

        # Create individual .bib file
        bib_entry_filename = f"bib_files/{cite_key}.bib"

        # subprocess.run(["bibtex-tidy",  "-m", bib_entry_filename])

        # Skip certain operations if --fast is set
        if not args.fast:
            with open(bib_entry_filename, "w") as bibfile:
                db = bibtexparser.bibdatabase.BibDatabase()
                db.entries = [entry]
                bibfile.write(writer.write(db))
            subprocess.run(["bibtex-tidy",  "-m", bib_entry_filename])

        # Create corresponding RST file
        rst_entry_filename = f"bib_entries/{cite_key}.rst"
        with open(rst_entry_filename, "w") as file:
            file.write(f"{cite_key}\n")
            file.write("=" * len(cite_key) + "\n\n")

            file.write(f":cite:t:`{cite_key}`\n\n")
            # Write the raw BibTeX entry
            file.write("**BibTeX Entry:**\n\n")
            file.write(".. code-block:: bibtex\n\n")
            # Read and write the content of the .bib file
            with open(bib_entry_filename, "r") as bibfile:
                for line in bibfile:
                    file.write(f"   {line}")
            file.write(f"\n`Back to index <../{parent_rst_html}>`_\n")

        # Add entry to the parent RST file under the correct section
        # parent_rst.write(f"- `{cite_key} <{rst_entry_filename}>`_\n")
        parent_rst.write(f"- :cite:t:`{cite_key}` : `{cite_key} <bib_entries/{cite_key}.html>`_\n")


# # Create or open the index file
# with open(parent_rst_name, "w") as index_file:
#     # Write the header for the index file
#     index_file.write("List by Citation Keys\n")
#     index_file.write("=======================\n\n")
#
#     # Add an introductory line or description if needed
#     index_file.write("Here is a list of all entries in the SPDEs-Bib database:\n\n")
#
#     # Create links to each entry's page
#     for entry in bib_database.entries:
#         cite_key = entry["ID"]
#         index_file.write(f"- :cite:t:`{cite_key}` : `{cite_key} <bib_entries/{cite_key}.html>`_\n")
