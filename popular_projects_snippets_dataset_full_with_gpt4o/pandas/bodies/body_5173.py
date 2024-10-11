# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# GH#47268 don't silently wrap around
with pytest.raises(OutOfBoundsTimedelta, match="without overflow"):
    Timedelta(1000000000000000000, unit="W")

with pytest.raises(OutOfBoundsTimedelta, match="without overflow"):
    Timedelta(1000000000000000000.0, unit="W")
