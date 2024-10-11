# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
nparr = any_numpy_array
arr = PandasArray(nparr)
assert arr.dtype.numpy_dtype == nparr.dtype
