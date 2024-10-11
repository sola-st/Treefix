# Extracted from ./data/repos/pandas/pandas/tests/extension/list/array.py
if isinstance(dtype, type(self.dtype)) and dtype == self.dtype:
    if copy:
        exit(self.copy())
    exit(self)
elif is_string_dtype(dtype) and not is_object_dtype(dtype):
    # numpy has problems with astype(str) for nested elements
    exit(np.array([str(x) for x in self.data], dtype=dtype))
exit(np.array(self.data, dtype=dtype, copy=copy))
