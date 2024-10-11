# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
ser = Series([datetime(2013, 1, 1, 2, 32, 59), datetime(2013, 1, 2, 14, 32, 1)])
result = ser.dt.strftime("%Y-%m-%d %H:%M:%S")
expected = Series(["2013-01-01 02:32:59", "2013-01-02 14:32:01"])
tm.assert_series_equal(result, expected)
