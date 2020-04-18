# A4 to A5

[![Build Status](https://travis-ci.org/nbeguier/a42a5.svg?branch=master)](https://travis-ci.org/nbeguier/a42a5) [![Python 3.4|3.8](https://img.shields.io/badge/python-3.4|3.8-green.svg)](https://www.python.org/) [![License](https://img.shields.io/github/license/nbeguier/a42a5?color=blue)](https://github.com/nbeguier/a42a5/blob/master/LICENSE)

This tool can convert AX pdf to A(X+1) pdf ! Useful to read large pdf on a reading device.

## Prerequisites

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
# python3 a42a5.py --help
usage: a42a5.py [-h] [--up UP] [--down DOWN] [--left LEFT] [--right RIGHT]
                [--inter INTER] [--reverse]
                input output

positional arguments:
  input          Input file
  output         Output file

optional arguments:
  -h, --help     show this help message and exit
  --up UP        Margin up
  --down DOWN    Margin down
  --left LEFT    Margin left
  --right RIGHT  Margin right
  --inter INTER  Intersection between two pages
  --reverse      Cut vertically rather than horizontally
```

## Examples

```bash
# Easy use
python3 a42a5.py PDF_Samples/example_A4.pdf output_A5.pdf

# More complex
python3 a42a5.py PDF_Samples/example_A4.pdf output_A5.pdf --up 100 --down 100 --left 10 --right 5 --inter 20

# Cut horizontally
python3 a42a5.py PDF_Samples/example_A4.pdf output_A5.pdf --reverse
```

# License
Licensed under the [Apache License](https://github.com/nbeguier/a42a5/blob/master/LICENSE), Version 2.0 (the "License").

# Copyright
Copyright 2019-2020 Nicolas Béguier; ([nbeguier](https://beguier.eu/nicolas/) - nicolas_beguier[at]hotmail[dot]com)
