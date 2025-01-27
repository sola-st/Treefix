# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = self.array_cls(data, freq="D")
result = arr._unbox_scalar(arr[0])
expected = arr._ndarray.dtype.type
assert isinstance(result, expected)

result = arr._unbox_scalar(NaT)
assert isinstance(result, expected)

msg = f"'value' should be a {self.scalar_type.__name__}."
with pytest.raises(ValueError, match=msg):
    arr._unbox_scalar("foo")
