# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
rng = date_range("4/13/2010", "5/6/2010")

rng_eastern = rng.tz_localize(tzstr)

rng_repr = repr(rng_eastern)
assert "2010-04-13 00:00:00" in rng_repr
