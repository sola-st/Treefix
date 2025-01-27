# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_combine_first.py

s0 = to_datetime(Series(["2010", np.NaN]))
s1 = to_datetime(Series([np.NaN, "2011"]))
rs = s0.combine_first(s1)
xp = to_datetime(Series(["2010", "2011"]))
tm.assert_series_equal(rs, xp)

s0 = to_datetime(Series(["2010", np.NaN]))
s1 = Series([np.NaN, "2011"])
rs = s0.combine_first(s1)

xp = Series([datetime(2010, 1, 1), "2011"], dtype="datetime64[ns]")

tm.assert_series_equal(rs, xp)
