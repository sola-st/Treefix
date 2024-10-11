# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.array([1, 2, 3], dtype=np.int64)
indexer = [0, -1, -2]

msg = r"'indices' contains values less than allowed \(-2 < -1\)"
with pytest.raises(ValueError, match=msg):
    algos.take(arr, indexer, allow_fill=True)

result = algos.take(arr, indexer)
expected = np.array([1, 3, 2], dtype=np.int64)
tm.assert_numpy_array_equal(result, expected)
