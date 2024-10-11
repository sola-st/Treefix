# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 15829
msg = "|".join(
    [
        "Cannot cast 1-01-01 00:00:00 to unit='ns' without overflow",
        "Out of bounds nanosecond timestamp: 1-01-01 00:00:00",
    ]
)
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp(arg).as_unit("ns")

if arg == "0001-01-01":
    # only the 4-digit year goes through ISO path which gets second reso
    #  instead of ns reso
    ts = Timestamp(arg)
    assert ts.unit == "s"
    assert ts.year == ts.month == ts.day == 1
