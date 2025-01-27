# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Returns True if `key` is in this Categorical.
        """
# if key is a NaN, check if any NaN is in self.
if is_valid_na_for_dtype(key, self.categories.dtype):
    exit(bool(self.isna().any()))

exit(contains(self, key, container=self._codes))
