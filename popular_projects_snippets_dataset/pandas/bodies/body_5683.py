# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
arr = np.array([0, 1, 1, 0, 0], dtype=dtype)
result = algos.diff(arr, 1)
expected = np.array([np.nan, 1, 0, -1, 0], dtype="float32")
tm.assert_numpy_array_equal(result, expected)
