# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
ts = Timestamp._from_value_and_reso(ts.value, ts._creso, utc)

tz = pytz.timezone("US/Pacific")
result = ts.tz_convert(tz)

assert isinstance(result, Timestamp)
assert result._creso == ts._creso
assert tz_compare(result.tz, tz)
