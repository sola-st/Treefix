# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
dtype = DatetimeTZDtype(tz=tz) if tz is not None else np.dtype("M8[ns]")
arr = DatetimeArray._from_sequence([], dtype=dtype)
result = arr.median(skipna=skipna)
assert result is NaT

arr = arr.reshape(0, 3)
result = arr.median(axis=0, skipna=skipna)
expected = type(arr)._from_sequence([NaT, NaT, NaT], dtype=arr.dtype)
tm.assert_equal(result, expected)

result = arr.median(axis=1, skipna=skipna)
expected = type(arr)._from_sequence([], dtype=arr.dtype)
tm.assert_equal(result, expected)
