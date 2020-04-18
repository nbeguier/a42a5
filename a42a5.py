#!/usr/bin/env python3
"""
A4 to A5

Copyright 2019-2020 Nicolas Béguier
Licensed under the Apache License
Written by Nicolas BEGUIER (nicolas_beguier@hotmail.com)
"""
# pylint: disable=too-many-locals

# Standard library imports
from argparse import ArgumentParser
# Related third party imports
from PyPDF2 import PdfFileReader, PdfFileWriter

VERSION = '1.0.1'

def split(input_file, output_file, filters=None, reverse=False):
    """ Split function """
    filters_dict = {'margin_up': 0,
                    'margin_down': 0,
                    'margin_right': 0,
                    'margin_left': 0,
                    'inter': 10}
    filters_dict.update(filters)
    pdf_in_up = open(input_file, 'rb')
    pdf_in_down = open(input_file, 'rb')
    pdf_reader_up = PdfFileReader(pdf_in_up)
    pdf_reader_down = PdfFileReader(pdf_in_down)
    pdf_writer = PdfFileWriter()

    for pagenum in range(pdf_reader_up.numPages):
        page_up = pdf_reader_up.getPage(pagenum)
        page_down = pdf_reader_down.getPage(pagenum)
        max_x = page_up.mediaBox.getUpperRight_x()
        max_y = page_up.mediaBox.getUpperRight_y()
        if reverse:
            max_x_resized = max_x - filters_dict['margin_right'] + filters_dict['margin_left']
            # PAGE LEFT
            page_up.cropBox.upperRight = (
                max_x_resized/2 + filters_dict['inter'], max_y - filters_dict['margin_up'])
            page_up.cropBox.lowerLeft = (
                filters_dict['margin_left'], filters_dict['margin_down'])
            # PAGE RIGHT
            page_down.cropBox.upperRight = (
                max_x - filters_dict['margin_right'], max_y - filters_dict['margin_up'])
            page_down.cropBox.lowerLeft = (
                max_x_resized/2 - filters_dict['inter'], filters_dict['margin_down'])
        else:
            max_y_resized = max_y - filters_dict['margin_up'] + filters_dict['margin_down']
            # PAGE UP
            page_up.cropBox.upperRight = (
                max_x - filters_dict['margin_right'], max_y - filters_dict['margin_up'])
            page_up.cropBox.lowerLeft = (
                filters_dict['margin_left'], max_y_resized/2 - filters_dict['inter'])
            # PAGE DOWN
            page_down.cropBox.upperRight = (
                max_x - filters_dict['margin_right'], max_y_resized/2 + filters_dict['inter'])
            page_down.cropBox.lowerLeft = (
                filters_dict['margin_left'], filters_dict['margin_down'])
        pdf_writer.addPage(page_up)
        pdf_writer.addPage(page_down)

    with open(output_file, 'wb') as pdf_out:
        pdf_writer.write(pdf_out)
    pdf_in_up.close()
    pdf_in_down.close()

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
