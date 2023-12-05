#!/usr/bin/env python3
#
# By Le Chen and Chatgpt
# chenle02@gmail.com / le.chen@auburn.edu
# Created at Mon Dec  4 09:24:30 PM EST 2023
#

import bibtexparser
import os

# Load BibTeX file
bibtex_file = "../All-test.bib"
page_name = "../Reference.rst"
with open(bibtex_file) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Create or open the index file
with open(page_name, 'w') as index_file:
    # Write the header for the index file
    index_file.write("Welcome to the SPDEs-Bib Index\n")
    index_file.write("=================================\n\n")

    # Add an introductory line or description if needed
    index_file.write("Here is a list of all entries in the SPDEs-Bib database:\n\n")

    # Create links to each entry's page
    for entry in bib_database.entries:
        cite_key = entry['ID']
        index_file.write(f"- `{cite_key} <bib_entries/{cite_key}.html>`_\n")

    # Optionally, add any additional sections or text you need
