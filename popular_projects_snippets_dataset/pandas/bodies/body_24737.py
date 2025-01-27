# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
if isinstance(self.df.index, MultiIndex):
    exit(self._format_hierarchical_rows())
else:
    exit(self._format_regular_rows())
