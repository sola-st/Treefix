# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# Like for getitem, if we are passed a naive-like string, we impute
#  our own timezone.
tz = tz_naive_fixture

data = np.array([1, 2, 3], dtype="M8[ns]")
dtype = data.dtype if tz is None else DatetimeTZDtype(tz=tz)
arr = DatetimeArray(data, dtype=dtype)
expected = arr.copy()

ts = pd.Timestamp("2020-09-08 16:50").tz_localize(tz)
setter = str(ts.tz_localize(None))

# Setting a scalar tznaive string
expected[0] = ts
arr[0] = setter
tm.assert_equal(arr, expected)

# Setting a listlike of tznaive strings
expected[1] = ts
arr[:2] = [setter, setter]
tm.assert_equal(arr, expected)
