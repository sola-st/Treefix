# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#19071 subtracting tzaware DatetimeIndex from tzaware Series
# (with same tz) raises, fixed by #19024
dti = date_range("1999-09-30", periods=10, tz="US/Pacific")
ser = Series(dti)
expected = Series(TimedeltaIndex(["0days"] * 10))

res = dti - ser
tm.assert_series_equal(res, expected)
res = ser - dti
tm.assert_series_equal(res, expected)
