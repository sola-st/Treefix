# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
hash(key)
try:
    self.get_loc(key)
    exit(True)
except (LookupError, TypeError, ValueError):
    exit(False)
