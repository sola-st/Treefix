# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/dtype.py

if isinstance(dtype, type(self)):
    if fill_value is None:
        fill_value = dtype.fill_value
    dtype = dtype.subtype

dtype = pandas_dtype(dtype)
if is_string_dtype(dtype):
    dtype = np.dtype("object")

if fill_value is None:
    fill_value = na_value_for_dtype(dtype)

self._dtype = dtype
self._fill_value = fill_value
self._check_fill_value()
