# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH: 36294
ser = pd.to_datetime(Series(["1969-01-01 09:00:00", "2016-01-01 09:00:00"]))
result = ser.dt.normalize()
expected = pd.to_datetime(Series(["1969-01-01", "2016-01-01"]))
tm.assert_series_equal(result, expected)
