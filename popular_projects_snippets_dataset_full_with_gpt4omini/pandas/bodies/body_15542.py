# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_between.py
ser = Series(period_range("2000-01-01", periods=10, freq="D"))
left, right = ser[[2, 7]]
result = ser.between(left, right)
expected = (ser >= left) & (ser <= right)
tm.assert_series_equal(result, expected)
