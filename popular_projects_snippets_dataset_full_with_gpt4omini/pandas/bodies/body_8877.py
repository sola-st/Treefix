# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_ndarray_backed.py
arr = PandasArray(np.array([1, 2]))
dtype = arr.dtype

shape = (3, 9)
result = PandasArray._empty(shape, dtype=dtype)
assert isinstance(result, PandasArray)
assert result.dtype == dtype
assert result.shape == shape
