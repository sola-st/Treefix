# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
arr = arr1d.reshape(1, -1)

# axis = None
assert arr.median() == arr1d.median()
assert arr.median(skipna=False) is NaT

# axis = 0
result = arr.median(axis=0)
expected = arr1d
tm.assert_equal(result, expected)

# Since column 3 is all-NaT, we get NaT there with or without skipna
result = arr.median(axis=0, skipna=False)
expected = arr1d
tm.assert_equal(result, expected)

# axis = 1
result = arr.median(axis=1)
expected = type(arr)._from_sequence([arr1d.median()])
tm.assert_equal(result, expected)

result = arr.median(axis=1, skipna=False)
expected = type(arr)._from_sequence([NaT], dtype=arr.dtype)
tm.assert_equal(result, expected)
