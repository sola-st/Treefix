# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# from system utc to real utc
ts = Timestamp("2001-01-05 11:56", tz=timezones.maybe_get_tz("dateutil/UTC"))
# check that the time hasn't changed.
assert ts == ts.tz_convert(dateutil.tz.tzutc())

# from system utc to real utc
ts = Timestamp("2001-01-05 11:56", tz=timezones.maybe_get_tz("dateutil/UTC"))
# check that the time hasn't changed.
assert ts == ts.tz_convert(dateutil.tz.tzutc())
