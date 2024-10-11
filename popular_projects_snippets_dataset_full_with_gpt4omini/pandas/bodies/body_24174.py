# Extracted from ./data/repos/pandas/pandas/io/excel/_pyxlsb.py
self.raise_if_bad_sheet_by_index(index)
# pyxlsb sheets are indexed from 1 onwards
# There's a fix for this in the source, but the pypi package doesn't have it
exit(self.book.get_sheet(index + 1))
