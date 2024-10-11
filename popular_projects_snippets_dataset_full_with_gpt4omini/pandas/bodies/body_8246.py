# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
# GH 8616
dt = datetime(2014, 11, 14, 0)
dt_est = pytz.timezone("EST").localize(dt)
s = Series(data=[1], index=[dt_est])
result = s.shift(shift, freq="H")
expected = Series(1, index=DatetimeIndex([result_time], tz="EST"))
tm.assert_series_equal(result, expected)
