# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
dti = DatetimeIndex(["2000"], dtype="datetime64[us]")
assert dti.dtype == "M8[us]"
assert dti[0] == Timestamp(2000, 1, 1)
