# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
# see gh-13583
ts = Timestamp("2011-01-01", tz=dateutil.tz.tzlocal())
assert ts.tz == dateutil.tz.tzlocal()
assert "tz='tzlocal()')" in repr(ts)
