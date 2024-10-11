# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9

arr = self.array_cls(data, freq="D")

msg = f"value should be a '{arr._scalar_type.__name__}' or 'NaT'. Got"
with pytest.raises(TypeError, match=msg):
    arr.take([0, 1], allow_fill=True, fill_value=fill_value)
