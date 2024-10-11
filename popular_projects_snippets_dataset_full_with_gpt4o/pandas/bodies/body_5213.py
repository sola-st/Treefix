# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# need to cast to since td is out of bounds for ns, so
#  so we would raise OverflowError without casting
other = Timedelta(days=1).as_unit("us")

# td is out of bounds for ns
result = td + other
assert result._creso == other._creso
assert result.days == td.days + 1

result = other + td
assert result._creso == other._creso
assert result.days == td.days + 1

result = td - other
assert result._creso == other._creso
assert result.days == td.days - 1

result = other - td
assert result._creso == other._creso
assert result.days == 1 - td.days

other2 = Timedelta(500)
msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td + other2
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    other2 + td
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td - other2
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    other2 - td
