# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH#31971, enforced in 2.0
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = self.array_cls(data, freq="D")

with pytest.raises(TypeError, match="value should be a"):
    arr.shift(1, fill_value=1)
