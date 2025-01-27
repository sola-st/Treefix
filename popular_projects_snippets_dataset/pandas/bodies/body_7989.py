# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_join.py
pi = period_range("1/1/2000", "1/20/2000", freq="D")

result = pi._outer_indexer(pi)
tm.assert_extension_array_equal(result[0], pi._values)
tm.assert_numpy_array_equal(result[1], np.arange(len(pi), dtype=np.intp))
tm.assert_numpy_array_equal(result[2], np.arange(len(pi), dtype=np.intp))
