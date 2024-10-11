# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
arr = arr1d

# manually verified result
expected = arr[0] + 0.4 * pd.Timedelta(days=1)

result = arr.mean()
assert result == expected
result = arr.mean(skipna=False)
assert result is NaT

result = arr.dropna().mean(skipna=False)
assert result == expected

result = arr.mean(axis=0)
assert result == expected
