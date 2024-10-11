# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#33573 our index should retain its freq
series = Series([], DatetimeIndex([], freq="D"), dtype=object)
key = Timestamp("2012-01-01")
series[key] = 47
expected = Series(47, DatetimeIndex([key], freq="D"))
tm.assert_series_equal(series, expected)
assert series.index.freq == expected.index.freq
