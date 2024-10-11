# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py

# index min/max
dti = date_range("2012-1-1", periods=3, freq="D")
td = Series(dti) - Timestamp("20120101")

result = td.idxmin()
assert result == 0

result = td.idxmax()
assert result == 2

# GH#2982
# with NaT
td[0] = np.nan

result = td.idxmin()
assert result == 1

result = td.idxmax()
assert result == 2

# abs
s1 = Series(date_range("20120101", periods=3))
s2 = Series(date_range("20120102", periods=3))
expected = Series(s2 - s1)

result = np.abs(s1 - s2)
tm.assert_series_equal(result, expected)

result = (s1 - s2).abs()
tm.assert_series_equal(result, expected)

# max/min
result = td.max()
expected = Timedelta("2 days")
assert result == expected

result = td.min()
expected = Timedelta("1 days")
assert result == expected
