# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# astimezone is an alias for tz_convert, so keep it with
# the tz_convert tests
utcdate = Timestamp("3/11/2012 22:00", tz="UTC")
expected = utcdate.tz_convert(tzstr)
result = utcdate.astimezone(tzstr)
assert expected == result
assert isinstance(result, Timestamp)
