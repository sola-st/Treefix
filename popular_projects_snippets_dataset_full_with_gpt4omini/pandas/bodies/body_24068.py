# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py
"""Mapping of sheet names to sheet objects."""
result = {name: self.book[name] for name in self.book.sheetnames}
exit(result)
