#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
""" A4 to A5 """

from argparse import ArgumentParser
import PyPDF2


def split(input_file, output_file, margin_up, margin_down, margin_left, margin_right, inter):
    """ Split func """
    pdf_in_up = open(input_file, 'rb')
    pdf_in_down = open(input_file, 'rb')
    pdf_reader_up = PyPDF2.PdfFileReader(pdf_in_up)
    pdf_reader_down = PyPDF2.PdfFileReader(pdf_in_down)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader_up.numPages):
        page_up = pdf_reader_up.getPage(pagenum)
        page_down = pdf_reader_down.getPage(pagenum)
        max_x = page_up.mediaBox.getUpperRight_x()
        max_y = page_up.mediaBox.getUpperRight_y()
        max_y_resized = max_y - margin_up + margin_down
        # PAGE UP
        page_up.cropBox.upperRight = (max_x - margin_right, max_y - margin_up)
        page_up.cropBox.lowerLeft = (margin_left, max_y_resized/2 - inter)
        # PAGE DOWN
        page_down.cropBox.upperRight = (max_x - margin_right, max_y_resized/2 + inter)
        page_down.cropBox.lowerLeft = (margin_left, margin_down)
        pdf_writer.addPage(page_up)
        pdf_writer.addPage(page_down)

    pdf_out = open(output_file, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in_up.close()
    pdf_in_down.close()

if __name__ == '__main__':
    CSV_ROOT_PATH = '.'
    PARSER = ArgumentParser()

    PARSER.add_argument('--input', '-i', action='store',
                        help='Input file')
    PARSER.add_argument('--output', '-o', action='store',
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

    ARGS = PARSER.parse_args()

    split(ARGS.input, ARGS.output,
          int(ARGS.up), int(ARGS.down), int(ARGS.left), int(ARGS.right),
          int(ARGS.inter))
