# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
dtype = PandasDtype(any_numpy_dtype)

result = PandasDtype(dtype)
assert result == dtype
