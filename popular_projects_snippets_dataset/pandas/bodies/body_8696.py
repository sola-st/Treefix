# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = self.array_cls(data, freq="D")
result = arr._scalar_from_string(str(arr[0]))
assert result == arr[0]
