# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
# NumPy has issues when all the dicts are the same length.
# np.array([UserDict(...), UserDict(...)]) fails,
# but np.array([{...}, {...}]) works, so cast.
from pandas.core.arrays.string_ import StringDtype

dtype = pandas_dtype(dtype)
# needed to add this check for the Series constructor
if isinstance(dtype, type(self.dtype)) and dtype == self.dtype:
    if copy:
        exit(self.copy())
    exit(self)
elif isinstance(dtype, StringDtype):
    value = self.astype(str)  # numpy doesn't like nested dicts
    exit(dtype.construct_array_type()._from_sequence(value, copy=False))

exit(np.array([dict(x) for x in self], dtype=dtype, copy=copy))
