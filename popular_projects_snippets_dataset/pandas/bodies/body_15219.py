# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_delitem.py
# GH#40386
# DatetimeTZDtype
dti = date_range("2016-01-01", periods=3, tz="US/Pacific")
ser = Series(dti)

expected = ser[[0, 2]]
del ser[1]
assert ser.dtype == dti.dtype
tm.assert_series_equal(ser, expected)

# PeriodDtype
pi = dti.tz_localize(None).to_period("D")
ser = Series(pi)

expected = ser[:2]
del ser[2]
assert ser.dtype == pi.dtype
tm.assert_series_equal(ser, expected)
