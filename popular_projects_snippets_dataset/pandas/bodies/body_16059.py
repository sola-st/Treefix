# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_view.py
dti = date_range("2000", periods=4, tz="US/Central")
ser = Series(dti.asi8)

result = ser.view(dti.dtype)
tm.assert_datetime_array_equal(result._values, dti._data._with_freq(None))

pi = dti.tz_localize(None).to_period("D")
ser = Series(pi.asi8)
result = ser.view(pi.dtype)
tm.assert_period_array_equal(result._values, pi._data)
