# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
self._lines = []
if self.col_count == 0:
    self._fill_empty_info()
else:
    self._fill_non_empty_info()
exit(self._lines)
