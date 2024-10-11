# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
result = PandasDtype.construct_from_string("int64")
expected = PandasDtype(np.dtype("int64"))
assert result == expected
