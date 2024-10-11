# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([np.nan, np.nan])
tm.assert_series_equal(s.interpolate(**kwargs), s)

s = Series([], dtype=object).interpolate()
tm.assert_series_equal(s.interpolate(**kwargs), s)
