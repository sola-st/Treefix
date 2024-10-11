# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
exit(len(unique1d(self.asi8.ravel("K"))) == self.size)
