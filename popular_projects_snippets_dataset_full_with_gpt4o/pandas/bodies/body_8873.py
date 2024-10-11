# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_ndarray_backed.py
ci = CategoricalIndex(["a", "b", "c"], ordered=True)
dtype = ci.dtype

# case with int8 codes
shape = (4,)
result = Categorical._empty(shape, dtype=dtype)
assert isinstance(result, Categorical)
assert result.shape == shape
assert result._ndarray.dtype == np.int8

# case where repr would segfault if we didn't override base implementation
result = Categorical._empty((4096,), dtype=dtype)
assert isinstance(result, Categorical)
assert result.shape == (4096,)
assert result._ndarray.dtype == np.int8
repr(result)

# case with int16 codes
ci = CategoricalIndex(list(range(512)) * 4, ordered=False)
dtype = ci.dtype
result = Categorical._empty(shape, dtype=dtype)
assert isinstance(result, Categorical)
assert result.shape == shape
assert result._ndarray.dtype == np.int16
