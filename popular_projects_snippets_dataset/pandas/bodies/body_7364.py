# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
msg = r"dtype timedelta64\[D\] cannot be converted to timedelta64\[ns\]"
with pytest.raises(ValueError, match=msg):
    TimedeltaIndex(["2000"], dtype="timedelta64[D]")

# "timedelta64[us]" was unsupported pre-2.0, but now this works.
tdi = TimedeltaIndex(["2000"], dtype="timedelta64[us]")
assert tdi.dtype == "m8[us]"
