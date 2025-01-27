# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Add line with range of indices to the table."""
self._lines.append(self.data.index._summary())
