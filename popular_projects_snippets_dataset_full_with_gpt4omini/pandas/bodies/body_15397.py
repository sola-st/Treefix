# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#10193
key = Timestamp("2012-01-01")
series = Series(dtype=object)
series[key] = 47
expected = Series(47, [key])
tm.assert_series_equal(series, expected)
