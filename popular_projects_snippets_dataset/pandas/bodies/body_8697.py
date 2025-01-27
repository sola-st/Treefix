# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = self.array_cls(data, freq="D")

msg = "does not support reduction 'not a method'"
with pytest.raises(TypeError, match=msg):
    arr._reduce("not a method")
