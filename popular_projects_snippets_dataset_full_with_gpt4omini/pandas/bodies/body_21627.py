# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if self.ndim > 1:
    exit((self[n] for n in range(len(self))))
else:
    exit((self._box_func(v) for v in self.asi8))
