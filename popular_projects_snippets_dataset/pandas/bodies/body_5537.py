# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# see gh-10758
msg = (
    "'NoneType' object cannot be interpreted as an integer"
    if PY310
    else "an integer is required"
)
with pytest.raises(TypeError, match=msg):
    Timestamp(2000, 1)

msg = "month must be in 1..12"
with pytest.raises(ValueError, match=msg):
    Timestamp(2000, 0, 1)
with pytest.raises(ValueError, match=msg):
    Timestamp(2000, 13, 1)

msg = "day is out of range for month"
with pytest.raises(ValueError, match=msg):
    Timestamp(2000, 1, 0)
with pytest.raises(ValueError, match=msg):
    Timestamp(2000, 1, 32)

# see gh-11630
assert repr(Timestamp(2015, 11, 12)) == repr(Timestamp("20151112"))
assert repr(Timestamp(2015, 11, 12, 1, 2, 3, 999999)) == repr(
    Timestamp("2015-11-12 01:02:03.999999")
)
