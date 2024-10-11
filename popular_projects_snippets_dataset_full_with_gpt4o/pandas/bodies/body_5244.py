# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
min_td = Timedelta(Timedelta.min)
max_td = Timedelta(Timedelta.max)

# GH 12727
# timedelta limits correspond to int64 boundaries
assert min_td.value == iNaT + 1
assert max_td.value == lib.i8max

# Beyond lower limit, a NAT before the Overflow
assert (min_td - Timedelta(1, "ns")) is NaT

msg = "int too (large|big) to convert"
with pytest.raises(OverflowError, match=msg):
    min_td - Timedelta(2, "ns")

with pytest.raises(OverflowError, match=msg):
    max_td + Timedelta(1, "ns")

# Same tests using the internal nanosecond values
td = Timedelta(min_td.value - 1, "ns")
assert td is NaT

msg = "Cannot cast -9223372036854775809 from ns to 'ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    Timedelta(min_td.value - 2, "ns")

msg = "Cannot cast 9223372036854775808 from ns to 'ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    Timedelta(max_td.value + 1, "ns")
