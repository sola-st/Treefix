# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
arr = arr1d[:0]

assert arr.mean(skipna=skipna) is NaT

arr2d = arr.reshape(0, 3)
result = arr2d.mean(axis=0, skipna=skipna)
expected = DatetimeArray._from_sequence([NaT, NaT, NaT], dtype=arr.dtype)
tm.assert_datetime_array_equal(result, expected)

result = arr2d.mean(axis=1, skipna=skipna)
expected = arr  # i.e. 1D, empty
tm.assert_datetime_array_equal(result, expected)

result = arr2d.mean(axis=None, skipna=skipna)
assert result is NaT
