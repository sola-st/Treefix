# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.arange(12).reshape(4, 3)
result = algos.take(arr, [0, -1])
expected = np.array([[0, 1, 2], [9, 10, 11]])
tm.assert_numpy_array_equal(result, expected)

# allow_fill=True
result = algos.take(arr, [0, -1], allow_fill=True, fill_value=0)
expected = np.array([[0, 1, 2], [0, 0, 0]])
tm.assert_numpy_array_equal(result, expected)
