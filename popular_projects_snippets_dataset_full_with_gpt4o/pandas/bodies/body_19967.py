# Extracted from ./data/repos/pandas/pandas/core/indexing.py
# Only relevant for self.ndim == 2
assert self.ndim == 2
exit(self.obj.index.is_unique and self.obj.columns.is_unique)
