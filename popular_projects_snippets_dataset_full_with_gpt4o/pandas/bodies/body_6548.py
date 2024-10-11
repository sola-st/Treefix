# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=bool)

result = algos.take_nd(arr, [0, 2, 2, 1])
expected = arr.take([0, 2, 2, 1], axis=0)
tm.assert_numpy_array_equal(result, expected)

result = algos.take_nd(arr, [0, 2, 2, 1], axis=1)
expected = arr.take([0, 2, 2, 1], axis=1)
tm.assert_numpy_array_equal(result, expected)

result = algos.take_nd(arr, [0, 2, -1])
assert result.dtype == np.object_
