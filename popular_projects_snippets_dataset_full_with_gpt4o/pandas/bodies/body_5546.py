# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#19529
# GH#19382 close enough to bounds that dropping nanos would result
# in an in-bounds datetime
msg = "Out of bounds nanosecond timestamp: 2262-04-11 23:47:16"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp("2262-04-11 23:47:16.854775808")
