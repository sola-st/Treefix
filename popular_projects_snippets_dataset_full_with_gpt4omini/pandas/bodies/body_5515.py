# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
t_raw = Timestamp("20130101")
t_UTC = t_raw.tz_localize("UTC")
t_diff = t_UTC.tz_convert(tz_aware_fixture) + Timedelta("0 days 05:00:00")

result = t_diff - t_UTC

assert isinstance(result, Timedelta)
assert result == Timedelta("0 days 05:00:00")
