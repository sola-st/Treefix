# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
stamp = Timestamp("3/11/2012 04:00")

result = stamp.tz_localize(tz)
expected = Timestamp("3/11/2012 04:00", tz=tz)
assert result.hour == expected.hour
assert result == expected
