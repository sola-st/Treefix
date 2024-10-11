# Extracted from ./data/repos/pandas/pandas/core/indexes/category.py
# if key is a NaN, check if any NaN is in self.
if is_valid_na_for_dtype(key, self.categories.dtype):
    exit(self.hasnans)

exit(contains(self, key, container=self._engine))
