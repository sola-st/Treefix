# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = DatetimeArray(data, freq="D").tz_localize("Asia/Tokyo")
if index:
    arr = pd.Index(arr)

expected = arr.searchsorted(arr[2])
result = arr.searchsorted(arr[2].tz_convert("UTC"))
assert result == expected

expected = arr.searchsorted(arr[2:6])
result = arr.searchsorted(arr[2:6].tz_convert("UTC"))
tm.assert_equal(result, expected)
