# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_tz_localize.py
# GH#2248
ser = Series(dtype=object)

ser2 = ser.tz_localize("utc")
assert ser2.index.tz == timezone.utc

ser2 = ser.tz_localize(tzstr)
timezones.tz_compare(ser2.index.tz, timezones.maybe_get_tz(tzstr))
