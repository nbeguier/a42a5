#!/usr/bin/env python3
"""
Merge multiple PDFs and JPEGs

Copyright 2019-2023 Nicolas Béguier
Licensed under the Apache License
Written by Nicolas BEGUIER (nicolas_beguier@hotmail.com)
"""
# Standard library imports
import io
import sys
from pathlib import Path

# Related third party imports
from PyPDF2 import PdfMerger, PdfReader
import img2pdf

# Debug
# from pdb import set_trace as st

VERSION = '0.0.2'

merger = PdfMerger()
for filename in sys.argv[1:]:
    file_path = Path(filename)
    if file_path.suffix.lower() == '.pdf':
        merger.append(PdfReader(file_path.open('rb')))
    elif file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
        jpg_content = file_path.read_bytes()
        pdf_content = img2pdf.convert(jpg_content)
        merger.append(PdfReader(io.BytesIO(pdf_content)))

merger.write('document-output.pdf')
