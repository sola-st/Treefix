# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
dtype = pandas_dtype(dtype)

if is_dtype_equal(dtype, self.dtype):
    if copy:
        exit(self.copy())
    exit(self)
elif isinstance(dtype, NumericDtype):
    data = self._data.cast(pa.from_numpy_dtype(dtype.numpy_dtype))
    exit(dtype.__from_arrow__(data))
elif isinstance(dtype, np.dtype) and np.issubdtype(dtype, np.floating):
    exit(self.to_numpy(dtype=dtype, na_value=np.nan))

exit(super().astype(dtype, copy=copy))
