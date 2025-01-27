# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
if type(self) is not type(other):
    exit(False)
if not is_dtype_equal(self.dtype, other.dtype):
    exit(False)
exit(bool(array_equivalent(self._ndarray, other._ndarray)))
