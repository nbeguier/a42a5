#A4 to A5

This is a fork of https://github.com/mstamy2/PyPDF2.


##Examples

```bash
# python a42a5.py --help
usage: a42a5.py [-h] [--input INPUT] [--output OUTPUT] [--up UP] [--down DOWN]
                [--left LEFT] [--right RIGHT] [--inter INTER]

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Input file
  --output OUTPUT, -o OUTPUT
                        Output file
  --up UP               Margin up
  --down DOWN           Margin down
  --left LEFT           Margin left
  --right RIGHT         Margin right
  --inter INTER         Intersection between two pages
```

```bash
# Easy use
python a42a5.py --input /home/Mastering-Bitcoin.pdf --output output.pdf

# More complex
python a42a5.py --input /home/Mastering-Bitcoin.pdf --output output.pdf --up 100 --down 100 --left 10 --right 5 --inter 20
```

