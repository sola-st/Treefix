# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# see GH#14088
s = Series([datetime(2016, 8, 23, 12, tzinfo=pytz.utc), NaT])
dt = datetime(2016, 8, 22, 12, tzinfo=pytz.utc)
exp = Series([Timedelta("1 days"), NaT])
tm.assert_series_equal(s - dt, exp)
tm.assert_series_equal(s - Timestamp(dt), exp)
