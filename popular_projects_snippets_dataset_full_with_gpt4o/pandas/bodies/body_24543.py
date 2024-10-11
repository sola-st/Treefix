# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""Preprocess elements of the row."""
if self.fmt.escape:
    crow = _escape_symbols(row)
else:
    crow = [x if x else "{}" for x in row]
if self.fmt.bold_rows and self.fmt.index:
    crow = _convert_to_bold(crow, self.index_levels)
exit(crow)
