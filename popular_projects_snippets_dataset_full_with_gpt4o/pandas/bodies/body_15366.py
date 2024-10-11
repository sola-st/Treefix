# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# https://github.com/pandas-dev/pandas/issues/35878
idx = MultiIndex.from_tuples([("a", 1), ("b", 2)])
result = Series([1, 2], index=idx)
expected = result.copy()
result.loc[[]] = 0
tm.assert_series_equal(result, expected)
