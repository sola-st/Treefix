# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#40110
arr = np.random.randn(2)

# Long-standing behavior (for Series, new in 2.0 for DataFrame)
#  has been to ignore the dtype on these;
#  not clear if this is what we want long-term
expected = frame_or_series(arr)

# GH#49599 as of 2.0 we raise instead of silently retaining float dtype
msg = "Trying to coerce float values to integer"
with pytest.raises(ValueError, match=msg):
    frame_or_series(arr, dtype="i8")

with pytest.raises(ValueError, match=msg):
    frame_or_series(list(arr), dtype="i8")

# pre-2.0, when we had NaNs, we silently ignored the integer dtype
arr[0] = np.nan
expected = frame_or_series(arr)

msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
with pytest.raises(IntCastingNaNError, match=msg):
    frame_or_series(arr, dtype="i8")

exc = IntCastingNaNError
if frame_or_series is Series:
    # TODO: try to align these
    exc = ValueError
    msg = "cannot convert float NaN to integer"
with pytest.raises(exc, match=msg):
    # same behavior if we pass list instead of the ndarray
    frame_or_series(list(arr), dtype="i8")

# float array that can be losslessly cast to integers
arr = np.array([1.0, 2.0], dtype="float64")
expected = frame_or_series(arr.astype("i8"))

obj = frame_or_series(arr, dtype="i8")
tm.assert_equal(obj, expected)

obj = frame_or_series(list(arr), dtype="i8")
tm.assert_equal(obj, expected)
