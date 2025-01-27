# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#40110 make DataFrame behavior with arraylike floating data and
#  inty dtype match Series behavior

arr = np.random.randn(10, 5)

# GH#49599 in 2.0 we raise instead of either
#  a) silently ignoring dtype and returningfloat (the old Series behavior) or
#  b) rounding (the old DataFrame behavior)
msg = "Trying to coerce float values to integers"
with pytest.raises(ValueError, match=msg):
    DataFrame(arr, dtype="i8")

df = DataFrame(arr.round(), dtype="i8")
assert (df.dtypes == "i8").all()

# with NaNs, we go through a different path with a different warning
arr[0, 0] = np.nan
msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
with pytest.raises(IntCastingNaNError, match=msg):
    DataFrame(arr, dtype="i8")
with pytest.raises(IntCastingNaNError, match=msg):
    Series(arr[0], dtype="i8")
# The future (raising) behavior matches what we would get via astype:
msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
with pytest.raises(IntCastingNaNError, match=msg):
    DataFrame(arr).astype("i8")
with pytest.raises(IntCastingNaNError, match=msg):
    Series(arr[0]).astype("i8")
