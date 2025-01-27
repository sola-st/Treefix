# Extracted from ./data/repos/pandas/pandas/io/excel/_odfreader.py
from odf.table import Table

self.raise_if_bad_sheet_by_name(name)
tables = self.book.getElementsByType(Table)

for table in tables:
    if table.getAttribute("name") == name:
        exit(table)

self.close()
raise ValueError(f"sheet {name} not found")
