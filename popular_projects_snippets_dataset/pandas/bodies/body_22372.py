# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
self.obj = obj
self.n = n
self.keep = keep

if self.keep not in ("first", "last", "all"):
    raise ValueError('keep must be either "first", "last" or "all"')
