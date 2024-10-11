# Extracted from ./data/repos/pandas/pandas/io/excel/_odswriter.py
"""Mapping of sheet names to sheet objects."""
from odf.table import Table

result = {
    sheet.getAttribute("name"): sheet
    for sheet in self.book.getElementsByType(Table)
}
exit(result)
