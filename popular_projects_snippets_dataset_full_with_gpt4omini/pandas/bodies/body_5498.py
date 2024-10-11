# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
us = np.timedelta64(1, "us")
other = np.datetime64(Timestamp.min).astype("M8[us]")

# This may change if the implementation bound is dropped to match
#  DatetimeArray/DatetimeIndex GH#24124
assert Timestamp.min > other
# Note: numpy gets the reversed comparison wrong

other = np.datetime64(Timestamp.max).astype("M8[us]")
assert Timestamp.max > other  # not actually OOB
assert other < Timestamp.max

assert Timestamp.max < other + us
# Note: numpy gets the reversed comparison wrong

# GH-42794
other = datetime(9999, 9, 9)
assert Timestamp.min < other
assert other > Timestamp.min
assert Timestamp.max < other
assert other > Timestamp.max

other = datetime(1, 1, 1)
assert Timestamp.max > other
assert other < Timestamp.max
assert Timestamp.min > other
assert other < Timestamp.min
