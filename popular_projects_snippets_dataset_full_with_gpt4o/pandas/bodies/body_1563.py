# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
times = date_range("2000-01-01", freq="10min", periods=100000)
ser = Series(range(100000), times)
result = ser.loc[datetime(1900, 1, 1) : datetime(2100, 1, 1)]
tm.assert_series_equal(result, ser)
