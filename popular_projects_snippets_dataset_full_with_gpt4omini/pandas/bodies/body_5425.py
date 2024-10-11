# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
val = np.int64(946_684_800_000_000_000).view("M8[ns]")
stamp = Timestamp(val.view("i8") + 500)
assert stamp.year == 2000
assert stamp.month == 1
assert stamp.microsecond == 0
assert stamp.nanosecond == 500

# GH 14415
val = np.iinfo(np.int64).min + 80_000_000_000_000
stamp = Timestamp(val)
assert stamp.year == 1677
assert stamp.month == 9
assert stamp.day == 21
assert stamp.microsecond == 145224
assert stamp.nanosecond == 192
