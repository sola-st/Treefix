# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
tstr = "2014-02-01 09:00"
ts = Timestamp(tstr)
local = ts.tz_localize("Asia/Tokyo")
assert local.hour == 9
assert local == Timestamp(tstr, tz="Asia/Tokyo")
conv = local.tz_convert("US/Eastern")
assert conv == Timestamp("2014-01-31 19:00", tz="US/Eastern")
assert conv.hour == 19

# preserves nanosecond
ts = Timestamp(tstr) + offsets.Nano(5)
local = ts.tz_localize("Asia/Tokyo")
assert local.hour == 9
assert local.nanosecond == 5
conv = local.tz_convert("US/Eastern")
assert conv.nanosecond == 5
assert conv.hour == 19
