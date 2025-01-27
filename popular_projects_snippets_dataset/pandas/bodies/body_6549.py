# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.random.randn(4, 3).astype(np.float32)
indexer = [0, 2, -1, 1, -1]

# axis=0
result = algos.take_nd(arr, indexer, axis=0)

expected = arr.take(indexer, axis=0)
expected[[2, 4], :] = np.nan
tm.assert_almost_equal(result, expected)

# axis=1
result = algos.take_nd(arr, indexer, axis=1)
expected = arr.take(indexer, axis=1)
expected[:, [2, 4]] = np.nan
tm.assert_almost_equal(result, expected)
