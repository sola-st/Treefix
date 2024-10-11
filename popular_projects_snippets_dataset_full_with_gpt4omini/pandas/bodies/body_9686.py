# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
arr = arr1d
arr = arr.as_unit(unit)
tz = arr.tz

result = arr.min()
expected = pd.Timestamp("2000-01-02", tz=tz).as_unit(unit)
assert result == expected
assert result.unit == expected.unit

result = arr.max()
expected = pd.Timestamp("2000-01-05", tz=tz).as_unit(unit)
assert result == expected
assert result.unit == expected.unit

result = arr.min(skipna=False)
assert result is NaT

result = arr.max(skipna=False)
assert result is NaT
