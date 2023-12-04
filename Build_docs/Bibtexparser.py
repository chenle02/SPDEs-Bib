#!/usr/bin/env python3
#
# By Le Chen and Chatgpt
# chenle02@gmail.com / le.chen@auburn.edu
# Created at Mon Dec  4 10:15:16 AM EST 2023
#

import bibtexparser

# Load BibTeX file
with open('../All.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Open a new RST file to write citations
with open('citations.rst', 'w') as file:
    file.write('Citations\n')
    file.write('=========\n\n')
    for entry in bib_database.entries:
        cite_key = entry['ID']
        file.write(f':cite:t:`{cite_key}`\n\n')
