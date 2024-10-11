# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.random.randn(10).astype(np.float32)

indexer = [1, 2, 3, -1]
result = algos.take_nd(arr, indexer)
expected = arr.take(indexer)
expected[-1] = np.nan
tm.assert_almost_equal(result, expected)
