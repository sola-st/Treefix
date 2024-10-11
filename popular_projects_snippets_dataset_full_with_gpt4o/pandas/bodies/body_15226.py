# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_where.py
# see gh-15414
s = Series([1, 2, 3])
cond = [False, True, True]
expected = Series([np.nan, 2, 3])

result = s.where(klass(cond))
tm.assert_series_equal(result, expected)
