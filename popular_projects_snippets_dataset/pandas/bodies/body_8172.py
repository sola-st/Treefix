# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
rng = date_range("3/11/2012", "3/12/2012", freq="H", tz="utc")
rng_eastern = rng.tz_convert(tz)

# Values are unmodified
tm.assert_numpy_array_equal(rng.asi8, rng_eastern.asi8)

assert timezones.tz_compare(rng_eastern.tz, timezones.maybe_get_tz(tz))
