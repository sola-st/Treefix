# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# numpy gets this wrong because of silent overflow
dt64 = np.datetime64(9223372800, "s")  # won't fit in M8[ns]
ts = Timestamp._from_dt64(dt64)

# subtracting 3600*24 gives a datetime64 that _can_ fit inside the
#  nanosecond implementation bounds.
other = Timestamp(dt64 - 3600 * 24).as_unit("ns")
assert other < ts
assert other.asm8 > ts.asm8  # <- numpy gets this wrong
assert ts > other
assert ts.asm8 < other.asm8  # <- numpy gets this wrong
assert not other == ts
assert ts != other
