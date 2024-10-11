# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
dtype = pandas_dtype(dtype)

if is_dtype_equal(dtype, self.dtype):
    if copy:
        exit(self.copy())
    exit(self)

elif isinstance(dtype, IntegerDtype):
    arr = self._ndarray.copy()
    mask = self.isna()
    arr[mask] = 0
    values = arr.astype(dtype.numpy_dtype)
    exit(IntegerArray(values, mask, copy=False))
elif isinstance(dtype, FloatingDtype):
    arr = self.copy()
    mask = self.isna()
    arr[mask] = "0"
    values = arr.astype(dtype.numpy_dtype)
    exit(FloatingArray(values, mask, copy=False))
elif isinstance(dtype, ExtensionDtype):
    exit(super().astype(dtype, copy=copy))
elif np.issubdtype(dtype, np.floating):
    arr = self._ndarray.copy()
    mask = self.isna()
    arr[mask] = 0
    values = arr.astype(dtype)
    values[mask] = np.nan
    exit(values)

exit(super().astype(dtype, copy))
