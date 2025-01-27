# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = self.array_cls(data, freq="D")

arr[0] = arr[1]
expected = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
expected[0] = expected[1]

tm.assert_numpy_array_equal(arr.asi8, expected)

arr[:2] = arr[-2:]
expected[:2] = expected[-2:]
tm.assert_numpy_array_equal(arr.asi8, expected)
