# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Add line with string representation of dataframe to the table."""
self._lines.append(str(type(self.data)))
