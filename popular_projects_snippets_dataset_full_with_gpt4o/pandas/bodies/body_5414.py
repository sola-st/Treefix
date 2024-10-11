# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
tz = tz_naive_fixture
# GH 13727
dt = Timestamp("2000-01-01 00:00:00", tz=tz)
assert dt.is_leap_year
assert isinstance(dt.is_leap_year, bool)

dt = Timestamp("1999-01-01 00:00:00", tz=tz)
assert not dt.is_leap_year

dt = Timestamp("2004-01-01 00:00:00", tz=tz)
assert dt.is_leap_year

dt = Timestamp("2100-01-01 00:00:00", tz=tz)
assert not dt.is_leap_year
