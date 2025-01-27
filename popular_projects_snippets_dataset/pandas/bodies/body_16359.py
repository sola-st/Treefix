# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
s = Series(index, dtype=object)
exp = Series(index).astype(object)
tm.assert_series_equal(s, exp)

s = Series(Index(index, dtype=object), dtype=object)
exp = Series(index).astype(object)
tm.assert_series_equal(s, exp)

s = Series(index.astype(object), dtype=object)
exp = Series(index).astype(object)
tm.assert_series_equal(s, exp)
