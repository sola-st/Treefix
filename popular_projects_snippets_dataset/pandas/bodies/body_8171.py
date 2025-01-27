# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH#13583
# tz_convert doesn't affect to internal
dti = date_range(start="2001-01-01", end="2001-03-01", tz="UTC")
dti2 = dti.tz_convert(dateutil.tz.tzlocal())
tm.assert_numpy_array_equal(dti2.asi8, dti.asi8)

dti = date_range(start="2001-01-01", end="2001-03-01", tz=dateutil.tz.tzlocal())
dti2 = dti.tz_convert(None)
tm.assert_numpy_array_equal(dti2.asi8, dti.asi8)
