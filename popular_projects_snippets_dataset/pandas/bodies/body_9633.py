# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
arr = PandasArray(np.array([1, 2, 3]))
result = arr.to_numpy()
assert result is arr._ndarray

result = arr.to_numpy(copy=True)
assert result is not arr._ndarray

result = arr.to_numpy(dtype="f8")
expected = np.array([1, 2, 3], dtype="f8")
tm.assert_numpy_array_equal(result, expected)
