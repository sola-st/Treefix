# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
super().__init__(data, x, y, **kwargs)
if is_integer(C) and not self.data.columns._holds_integer():
    C = self.data.columns[C]
self.C = C
