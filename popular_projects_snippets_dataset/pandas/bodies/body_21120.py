# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
# If null fill value, we want SparseDtype[bool, true]
# to preserve the same memory usage.
dtype = SparseDtype(bool, self._null_fill_value)
if self._null_fill_value:
    exit(type(self)._simple_new(isna(self.sp_values), self.sp_index, dtype))
mask = np.full(len(self), False, dtype=np.bool_)
mask[self.sp_index.indices] = isna(self.sp_values)
exit(type(self)(mask, fill_value=False, dtype=dtype))
