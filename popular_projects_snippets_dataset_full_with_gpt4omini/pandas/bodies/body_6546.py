# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.random.randn(10, 5).astype(np.float32)

indexer = [1, 2, 3, -1]

# axis=0
result = algos.take_nd(arr, indexer, axis=0)
expected = arr.take(indexer, axis=0)
expected[-1] = np.nan
tm.assert_almost_equal(result, expected)

# axis=1
result = algos.take_nd(arr, indexer, axis=1)
expected = arr.take(indexer, axis=1)
expected[:, -1] = np.nan
tm.assert_almost_equal(result, expected)
