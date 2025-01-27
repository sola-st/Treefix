# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
data = np.arange(10).astype(float)
out = np.mean(SparseArray(data))
assert out == 4.5

data[5] = np.nan
out = np.mean(SparseArray(data))
assert out == 40.0 / 9

msg = "the 'dtype' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.mean(SparseArray(data), dtype=np.int64)

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.mean(SparseArray(data), out=out)
