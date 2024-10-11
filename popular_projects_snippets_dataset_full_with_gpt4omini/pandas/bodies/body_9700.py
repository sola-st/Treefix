# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
arr = DatetimeArray(
    np.array(["2000-01-01T06:00:00"], dtype="M8[ns]"),
    dtype=DatetimeTZDtype(tz="US/Central"),
)
dtype = DatetimeTZDtype(tz="US/Eastern")
msg = r"dtype=datetime64\[ns.*\] does not match data dtype datetime64\[ns.*\]"
with pytest.raises(TypeError, match=msg):
    DatetimeArray(arr, dtype=dtype)

# also with mismatched tzawareness
with pytest.raises(TypeError, match=msg):
    DatetimeArray(arr, dtype=np.dtype("M8[ns]"))
with pytest.raises(TypeError, match=msg):
    DatetimeArray(arr.tz_localize(None), dtype=arr.dtype)
