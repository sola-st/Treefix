# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH11708
base = to_datetime("2013-01-01 00:00:00", cache=cache)
base = base.tz_localize("UTC").tz_convert(tz)
dt_time = to_datetime(dt_string, cache=cache)
assert base == dt_time
assert dt_string_repr == repr(dt_time)
