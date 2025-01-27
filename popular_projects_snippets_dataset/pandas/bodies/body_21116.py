# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
if self._null_fill_value:
    exit(isna(fill_value))
else:
    exit(self.fill_value == fill_value)
