# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
dr = date_range(start="1/1/2012", freq="5min", periods=10)

# BAD Example, datetimes first
ser = Series(np.arange(10), index=[dr, np.arange(10)])
grouped = ser.groupby(lambda x: x[1] % 2 == 0)
result = grouped.count()

ser = Series(np.arange(10), index=[np.arange(10), dr])
grouped = ser.groupby(lambda x: x[0] % 2 == 0)
expected = grouped.count()

tm.assert_series_equal(result, expected)
