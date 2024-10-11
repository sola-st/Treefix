# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 10758
msg = "function missing required argument 'day'|Required argument 'day'"
with pytest.raises(TypeError, match=msg):
    Timestamp(year=2000, month=1)

msg = "month must be in 1..12"
with pytest.raises(ValueError, match=msg):
    Timestamp(year=2000, month=0, day=1)
with pytest.raises(ValueError, match=msg):
    Timestamp(year=2000, month=13, day=1)

msg = "day is out of range for month"
with pytest.raises(ValueError, match=msg):
    Timestamp(year=2000, month=1, day=0)
with pytest.raises(ValueError, match=msg):
    Timestamp(year=2000, month=1, day=32)

assert repr(Timestamp(year=2015, month=11, day=12)) == repr(
    Timestamp("20151112")
)

assert repr(
    Timestamp(
        year=2015,
        month=11,
        day=12,
        hour=1,
        minute=2,
        second=3,
        microsecond=999999,
    )
) == repr(Timestamp("2015-11-12 01:02:03.999999"))
