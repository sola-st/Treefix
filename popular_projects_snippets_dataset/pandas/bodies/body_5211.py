# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
assert td // td == 1
assert (2.5 * td) // td == 2

other = Timedelta(td.value)
msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td // other

# Timedelta(other.to_pytimedelta()) has microsecond resolution,
#  so the floordiv doesn't require casting all the way to nanos,
#  so succeeds
res = other.to_pytimedelta() // td
assert res == 0

# if there's no overflow, we cast to the higher reso
left = Timedelta._from_value_and_reso(50050, NpyDatetimeUnit.NPY_FR_us.value)
right = Timedelta._from_value_and_reso(50, NpyDatetimeUnit.NPY_FR_ms.value)
result = left // right
assert result == 1
result = right // left
assert result == 0
