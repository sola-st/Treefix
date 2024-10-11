# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
if is_dtype_equal(dtype, self._dtype):
    if not copy:
        exit(self)
dtype = pandas_dtype(dtype)
if isinstance(dtype, type(self.dtype)):
    exit(type(self)(self._data, copy=copy, context=dtype.context))

exit(super().astype(dtype, copy=copy))
