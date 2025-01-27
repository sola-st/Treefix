# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d
if len(arr) % 2 == 0:
    # make it easier to define `expected`
    arr = arr[:-1]

expected = arr[len(arr) // 2]

result = arr.median()
assert type(result) is type(expected)
assert result == expected

arr[len(arr) // 2] = NaT
if not isinstance(expected, Period):
    expected = arr[len(arr) // 2 - 1 : len(arr) // 2 + 2].mean()

assert arr.median(skipna=False) is NaT

result = arr.median()
assert type(result) is type(expected)
assert result == expected

assert arr[:0].median() is NaT
assert arr[:0].median(skipna=False) is NaT

# 2d Case
arr2 = arr.reshape(-1, 1)

result = arr2.median(axis=None)
assert type(result) is type(expected)
assert result == expected

assert arr2.median(axis=None, skipna=False) is NaT

result = arr2.median(axis=0)
expected2 = type(arr)._from_sequence([expected], dtype=arr.dtype)
tm.assert_equal(result, expected2)

result = arr2.median(axis=0, skipna=False)
expected2 = type(arr)._from_sequence([NaT], dtype=arr.dtype)
tm.assert_equal(result, expected2)

result = arr2.median(axis=1)
tm.assert_equal(result, arr)

result = arr2.median(axis=1, skipna=False)
tm.assert_equal(result, arr)
