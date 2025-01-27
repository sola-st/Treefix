# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH 8856
mi = MultiIndex.from_product(([0, 1], list("abcde")))
result = Series(np.arange(10, dtype=np.int64), mi)
indexer_sli(result)[::4] = 100
expected = Series([100, 1, 2, 3, 100, 5, 6, 7, 100, 9], mi)
tm.assert_series_equal(result, expected)
