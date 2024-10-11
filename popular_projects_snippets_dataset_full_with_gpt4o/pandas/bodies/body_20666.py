# Extracted from ./data/repos/pandas/pandas/core/indexes/frozen.py
if isinstance(n, slice):
    exit(type(self)(super().__getitem__(n)))
exit(super().__getitem__(n))
