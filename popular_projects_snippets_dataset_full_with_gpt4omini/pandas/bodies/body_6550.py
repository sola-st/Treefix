# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
# 2005/01/01 - 2006/01/01
arr = np.random.randint(11_045_376, 11_360_736, (5, 3)) * 100_000_000_000
arr = arr.view(dtype="datetime64[ns]")
indexer = [0, 2, -1, 1, -1]

# axis=0
result = algos.take_nd(arr, indexer, axis=0)
expected = arr.take(indexer, axis=0)
expected.view(np.int64)[[2, 4], :] = iNaT
tm.assert_almost_equal(result, expected)

result = algos.take_nd(arr, indexer, axis=0, fill_value=datetime(2007, 1, 1))
expected = arr.take(indexer, axis=0)
expected[[2, 4], :] = datetime(2007, 1, 1)
tm.assert_almost_equal(result, expected)

# axis=1
result = algos.take_nd(arr, indexer, axis=1)
expected = arr.take(indexer, axis=1)
expected.view(np.int64)[:, [2, 4]] = iNaT
tm.assert_almost_equal(result, expected)

result = algos.take_nd(arr, indexer, axis=1, fill_value=datetime(2007, 1, 1))
expected = arr.take(indexer, axis=1)
expected[:, [2, 4]] = datetime(2007, 1, 1)
tm.assert_almost_equal(result, expected)
