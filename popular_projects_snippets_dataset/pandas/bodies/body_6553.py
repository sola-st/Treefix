# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.array([1, 2, 3])
indexer = np.array([1, -1])
with pytest.raises(ValueError, match="fill_value must be a scalar"):
    algos.take(arr, indexer, allow_fill=True, fill_value=[1])

# with object dtype it is allowed
arr = np.array([1, 2, 3], dtype=object)
result = algos.take(arr, indexer, allow_fill=True, fill_value=[1])
expected = np.array([2, [1]], dtype=object)
tm.assert_numpy_array_equal(result, expected)
