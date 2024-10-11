# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
data = np.arange(10).astype(float)
out = np.sum(SparseArray(data))
assert out == 45.0

data[5] = np.nan
out = np.sum(SparseArray(data, fill_value=2))
assert out == 40.0

out = np.sum(SparseArray(data, fill_value=np.nan))
assert out == 40.0

msg = "the 'dtype' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.sum(SparseArray(data), dtype=np.int64)

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.sum(SparseArray(data), out=out)
