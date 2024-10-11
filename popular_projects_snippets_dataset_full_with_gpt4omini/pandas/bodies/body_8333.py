# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
# GH#1475
msg = (
    "^Out of bounds nanosecond timestamp: "
    "1400-01-01( 00:00:00)?, at position 0$"
)
with pytest.raises(OutOfBoundsDatetime, match=msg):
    DatetimeIndex(data)
