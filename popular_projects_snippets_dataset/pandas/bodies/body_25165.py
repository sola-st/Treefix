# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if s is None:
    # hide the matplotlib default for size, in case we want to change
    # the handling of this argument later
    s = 20
elif is_hashable(s) and s in data.columns:
    s = data[s]
super().__init__(data, x, y, s=s, **kwargs)
if is_integer(c) and not self.data.columns._holds_integer():
    c = self.data.columns[c]
self.c = c
