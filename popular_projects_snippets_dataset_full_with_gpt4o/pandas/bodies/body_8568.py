# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 23986
msg = "Unexpected value for 'dtype'"
with pytest.raises(ValueError, match=msg):
    DatetimeIndex([1, 2], dtype=dtype)
