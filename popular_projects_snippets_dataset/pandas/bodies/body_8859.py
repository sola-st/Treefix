# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2000", periods=2, freq="D", tz="US/Central")
arr = DatetimeArray(dti)

repeated = arr.repeat([1, 1])

# preserves tz and values, but not freq
expected = DatetimeArray(arr.asi8, freq=None, dtype=arr.dtype)
tm.assert_equal(repeated, expected)
