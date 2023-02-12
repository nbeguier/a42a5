#!/usr/bin/env python3
"""
Merge multiple PDFs

Copyright 2019-2023 Nicolas Béguier
Licensed under the Apache License
Written by Nicolas BEGUIER (nicolas_beguier@hotmail.com)
"""
# Standard library imports
import sys
from pathlib import Path

# Related third party imports
from PyPDF2 import PdfMerger, PdfReader

# Debug
# from pdb import set_trace as st

VERSION = '0.0.1'

merger = PdfMerger()
for filename in sys.argv[1:]:
    file_path = Path(filename)
    merger.append(PdfReader(file_path.open('rb')))

merger.write('document-output.pdf')
