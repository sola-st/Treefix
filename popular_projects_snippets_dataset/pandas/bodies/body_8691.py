# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9

arr = self.array_cls(data, freq="D")

result = arr.take([-1, 1], allow_fill=True, fill_value=None)
assert result[0] is NaT

result = arr.take([-1, 1], allow_fill=True, fill_value=np.nan)
assert result[0] is NaT

result = arr.take([-1, 1], allow_fill=True, fill_value=NaT)
assert result[0] is NaT
