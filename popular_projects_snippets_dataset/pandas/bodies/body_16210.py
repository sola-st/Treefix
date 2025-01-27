# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# Ensures it doesn't fail to create the right series
# reported in issue#16726
series = Series(date_range("2012-01-01", periods=3))
offset = pd.offsets.DateOffset(days=6)
result = series - offset
expected = Series(pd.to_datetime(["2011-12-26", "2011-12-27", "2011-12-28"]))
tm.assert_series_equal(result, expected)
