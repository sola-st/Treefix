# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH#13583
offset = dateutil.tz.tzlocal().utcoffset(datetime(2011, 1, 1))
offset = int(offset.total_seconds() * 1000000000)

dti = date_range(start="2001-01-01", end="2001-03-01")
dti2 = dti.tz_localize(dateutil.tz.tzlocal())
tm.assert_numpy_array_equal(dti2.asi8 + offset, dti.asi8)

dti = date_range(start="2001-01-01", end="2001-03-01", tz=dateutil.tz.tzlocal())
dti2 = dti.tz_localize(None)
tm.assert_numpy_array_equal(dti2.asi8 - offset, dti.asi8)
