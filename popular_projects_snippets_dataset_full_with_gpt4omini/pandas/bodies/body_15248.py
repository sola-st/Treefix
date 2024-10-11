# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_set_value.py
# GH#1561

dates = [datetime(2001, 1, 1), datetime(2001, 1, 2)]
index = DatetimeIndex(dates)

s = Series(dtype=object)
s._set_value(dates[0], 1.0)
s._set_value(dates[1], np.nan)

expected = Series([1.0, np.nan], index=index)

tm.assert_series_equal(s, expected)
