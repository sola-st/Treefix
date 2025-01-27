# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

# basic
td = Series([timedelta(days=i) for i in range(3)])
assert td.dtype == "timedelta64[ns]"

td = Series([timedelta(days=1)])
assert td.dtype == "timedelta64[ns]"

td = Series([timedelta(days=1), timedelta(days=2), np.timedelta64(1, "s")])

assert td.dtype == "timedelta64[ns]"

# mixed with NaT
td = Series([timedelta(days=1), NaT], dtype="m8[ns]")
assert td.dtype == "timedelta64[ns]"

td = Series([timedelta(days=1), np.nan], dtype="m8[ns]")
assert td.dtype == "timedelta64[ns]"

td = Series([np.timedelta64(300000000), NaT], dtype="m8[ns]")
assert td.dtype == "timedelta64[ns]"

# improved inference
# GH5689
td = Series([np.timedelta64(300000000), NaT])
assert td.dtype == "timedelta64[ns]"

# because iNaT is int, not coerced to timedelta
td = Series([np.timedelta64(300000000), iNaT])
assert td.dtype == "object"

td = Series([np.timedelta64(300000000), np.nan])
assert td.dtype == "timedelta64[ns]"

td = Series([NaT, np.timedelta64(300000000)])
assert td.dtype == "timedelta64[ns]"

td = Series([np.timedelta64(1, "s")])
assert td.dtype == "timedelta64[ns]"

# valid astype
td.astype("int64")

# invalid casting
msg = r"Converting from timedelta64\[ns\] to int32 is not supported"
with pytest.raises(TypeError, match=msg):
    td.astype("int32")

# this is an invalid casting
msg = "|".join(
    [
        "Could not convert object to NumPy timedelta",
        "Could not convert 'foo' to NumPy timedelta",
    ]
)
with pytest.raises(ValueError, match=msg):
    Series([timedelta(days=1), "foo"], dtype="m8[ns]")

# leave as object here
td = Series([timedelta(days=i) for i in range(3)] + ["foo"])
assert td.dtype == "object"

# as of 2.0, these no longer infer timedelta64 based on the strings,
#  matching Index behavior
ser = Series([None, NaT, "1 Day"])
assert ser.dtype == object

ser = Series([np.nan, NaT, "1 Day"])
assert ser.dtype == object

ser = Series([NaT, None, "1 Day"])
assert ser.dtype == object

ser = Series([NaT, np.nan, "1 Day"])
assert ser.dtype == object
