# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = self.array_cls(data, freq="D")
arr[4] = NaT

fill_value = arr[3] if method == "pad" else arr[5]

result = arr.fillna(method=method)
assert result[4] == fill_value

# check that the original was not changed
assert arr[4] is NaT
