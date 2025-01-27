# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
arr = arr1d

result = arr.median()
assert result == arr[0]
result = arr.median(skipna=False)
assert result is NaT

result = arr.dropna().median(skipna=False)
assert result == arr[0]

result = arr.median(axis=0)
assert result == arr[0]
