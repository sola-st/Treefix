# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
arr = np.array([1, 2, 3], dtype="int64")
result = PandasArray._from_sequence(arr, dtype="uint64")
expected = PandasArray(np.array([1, 2, 3], dtype="uint64"))
tm.assert_extension_array_equal(result, expected)
