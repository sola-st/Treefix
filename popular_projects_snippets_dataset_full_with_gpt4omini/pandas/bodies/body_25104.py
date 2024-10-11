# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/misc.py
a = min(series)
b = max(series)
exit((series - a) / (b - a))
