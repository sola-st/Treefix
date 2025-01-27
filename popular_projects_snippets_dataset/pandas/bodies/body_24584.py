# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""Select proper table builder."""
if self.longtable:
    exit(LongTableBuilder)
if any([self.caption, self.label, self.position]):
    exit(RegularTableBuilder)
exit(TabularBuilder)
