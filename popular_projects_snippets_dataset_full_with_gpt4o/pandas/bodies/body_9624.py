# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
dtype = PandasDtype(np.dtype("int64"))
assert repr(dtype) == "PandasDtype('int64')"
