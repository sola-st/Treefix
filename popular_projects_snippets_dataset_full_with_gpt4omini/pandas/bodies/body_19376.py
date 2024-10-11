# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
# _hash_categories returns a uint64, so use the negative
# space for when we have unknown categories to avoid a conflict
if self.categories is None:
    if self.ordered:
        exit(-1)
    else:
        exit(-2)
        # We *do* want to include the real self.ordered here
exit(int(self._hash_categories))
