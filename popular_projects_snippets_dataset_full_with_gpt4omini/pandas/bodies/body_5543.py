# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#26651 check that we raise OutOfBoundsDatetime, not OverflowError
msg = str(Timestamp.max.value * 2)
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp(Timestamp.max.value * 2)
msg = str(Timestamp.min.value * 2)
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp(Timestamp.min.value * 2)
