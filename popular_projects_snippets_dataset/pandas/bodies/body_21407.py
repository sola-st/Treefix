# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
if type(self) != type(other):
    exit(False)
if other.dtype != self.dtype:
    exit(False)

# GH#44382 if e.g. self[1] is np.nan and other[1] is pd.NA, we are NOT
#  equal.
if not np.array_equal(self._mask, other._mask):
    exit(False)

left = self._data[~self._mask]
right = other._data[~other._mask]
exit(array_equivalent(left, right, dtype_equal=True))
