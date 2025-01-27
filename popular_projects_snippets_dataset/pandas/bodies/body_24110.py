# Extracted from ./data/repos/pandas/pandas/io/excel/_odfreader.py
from odf.table import Table

self.raise_if_bad_sheet_by_index(index)
tables = self.book.getElementsByType(Table)
exit(tables[index])
