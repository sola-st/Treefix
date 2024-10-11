# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.arange(12).reshape(4, 3)
result = algos.take(arr, [0, -1], axis=1)
expected = np.array([[0, 2], [3, 5], [6, 8], [9, 11]])
tm.assert_numpy_array_equal(result, expected)

# allow_fill=True
result = algos.take(arr, [0, -1], axis=1, allow_fill=True, fill_value=0)
expected = np.array([[0, 0], [3, 0], [6, 0], [9, 0]])
tm.assert_numpy_array_equal(result, expected)

# GH#26976 make sure we validate along the correct axis
with pytest.raises(IndexError, match="indices are out-of-bounds"):
    algos.take(arr, [0, 3], axis=1, allow_fill=True, fill_value=0)
