# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = self.array_cls(data, freq="D")
val = arr[0]

with pytest.raises(IndexError, match="index 12 is out of bounds"):
    arr[12] = val

with pytest.raises(TypeError, match="value should be a.* 'object'"):
    arr[0] = object()

msg = "cannot set using a list-like indexer with a different length"
with pytest.raises(ValueError, match=msg):
    # GH#36339
    arr[[]] = [arr[1]]

msg = "cannot set using a slice indexer with a different length than"
with pytest.raises(ValueError, match=msg):
    # GH#36339
    arr[1:1] = arr[:3]
