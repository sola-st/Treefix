# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_delitem.py
# GH#5542
# should delete the item inplace
s = Series(range(5))
del s[0]

expected = Series(range(1, 5), index=range(1, 5))
tm.assert_series_equal(s, expected)

del s[1]
expected = Series(range(2, 5), index=range(2, 5))
tm.assert_series_equal(s, expected)

# only 1 left, del, add, del
s = Series(1)
del s[0]
tm.assert_series_equal(s, Series(dtype="int64", index=Index([], dtype="int64")))
s[0] = 1
tm.assert_series_equal(s, Series(1))
del s[0]
tm.assert_series_equal(s, Series(dtype="int64", index=Index([], dtype="int64")))
