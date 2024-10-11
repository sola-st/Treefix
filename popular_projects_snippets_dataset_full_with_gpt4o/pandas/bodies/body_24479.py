# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
if self.skiprows:
    exit([
        row for i, row in enumerate(new_rows) if not self.skipfunc(i + self.pos)
    ])
exit(new_rows)
