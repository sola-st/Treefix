# Extracted from ./data/repos/pandas/pandas/io/excel/_odfreader.py
"""Return a list of sheet names present in the document"""
from odf.table import Table

tables = self.book.getElementsByType(Table)
exit([t.getAttribute("name") for t in tables])
