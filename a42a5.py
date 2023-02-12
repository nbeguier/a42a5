#!/usr/bin/env python3
"""
A4 to A5

Copyright 2019-2023 Nicolas Béguier
Licensed under the Apache License
Written by Nicolas BEGUIER (nicolas_beguier@hotmail.com)
"""
# pylint: disable=too-many-locals

# Standard library imports
from argparse import ArgumentParser
from pathlib import Path

# Related third party imports
from PyPDF2 import PdfReader, PdfWriter

VERSION = '1.1.0'

def split(input_file, output_file, filters=None, reverse=False):
    """ Split function """
    filters_dict = {'margin_up': 0,
                    'margin_down': 0,
                    'margin_right': 0,
                    'margin_left': 0,
                    'inter': 10}
    filters_dict.update(filters)
    pdf_in_up = Path(input_file).open('rb')
    pdf_in_down = Path(input_file).open('rb')
    pdf_reader_up = PdfReader(pdf_in_up)
    pdf_reader_down = PdfReader(pdf_in_down)
    pdf_writer = PdfWriter()

    for pagenum in range(len(pdf_reader_up.pages)):
        page_up = pdf_reader_up.pages[pagenum]
        page_down = pdf_reader_down.pages[pagenum]
        max_x = page_up.mediabox.right
        max_y = page_up.mediabox.top
        if reverse:
            max_x_resized = max_x - filters_dict['margin_right'] + filters_dict['margin_left']
            # PAGE LEFT
            page_up.cropbox.upper_right = (
                max_x_resized/2 + filters_dict['inter'], max_y - filters_dict['margin_up'])
            page_up.cropbox.lower_left = (
                filters_dict['margin_left'], filters_dict['margin_down'])
            # PAGE RIGHT
            page_down.cropbox.upper_right = (
                max_x - filters_dict['margin_right'], max_y - filters_dict['margin_up'])
            page_down.cropbox.lower_left = (
                max_x_resized/2 - filters_dict['inter'], filters_dict['margin_down'])
        else:
            max_y_resized = max_y - filters_dict['margin_up'] + filters_dict['margin_down']
            # PAGE UP
            page_up.cropbox.upper_right = (
                max_x - filters_dict['margin_right'], max_y - filters_dict['margin_up'])
            page_up.cropbox.lower_left = (
                filters_dict['margin_left'], max_y_resized/2 - filters_dict['inter'])
            # PAGE DOWN
            page_down.cropbox.upper_right = (
                max_x - filters_dict['margin_right'], max_y_resized/2 + filters_dict['inter'])
            page_down.cropbox.lower_left = (
                filters_dict['margin_left'], filters_dict['margin_down'])
        pdf_writer.add_page(page_up)
        pdf_writer.add_page(page_down)

    output_path = Path(output_file).open('wb')
    pdf_writer.write(output_path)

if __name__ == '__main__':
    CSV_ROOT_PATH = '.'
    PARSER = ArgumentParser()

    PARSER.add_argument('--version', action='version', version=VERSION)

    PARSER.add_argument('input', action='store',
                        help='Input file')
    PARSER.add_argument('output', action='store',
                        help='Output file')
    PARSER.add_argument('--up', default=0, action='store',
                        help='Margin up')
    PARSER.add_argument('--down', default=0, action='store',
                        help='Margin down')
    PARSER.add_argument('--left', default=0, action='store',
                        help='Margin left')
    PARSER.add_argument('--right', default=0, action='store',
                        help='Margin right')
    PARSER.add_argument('--inter', default=10, action='store',
                        help='Intersection between two pages')
    PARSER.add_argument('--reverse', default=False, action='store_true',
                        help='Cut vertically rather than horizontally')

    ARGS = PARSER.parse_args()

    split(ARGS.input, ARGS.output, filters={'margin_up': int(ARGS.up),
                                            'margin_down': int(ARGS.down),
                                            'margin_right': int(ARGS.right),
                                            'margin_left': int(ARGS.left),
                                            'inter': int(ARGS.inter)}, reverse=ARGS.reverse)
