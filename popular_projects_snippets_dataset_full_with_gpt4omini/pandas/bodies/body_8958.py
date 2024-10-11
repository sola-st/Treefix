# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
# GH#17570
out = np.any(SparseArray(data))
assert out

out = np.any(SparseArray(data, fill_value=pos))
assert out

data[1] = neg
out = np.any(SparseArray(data))
assert not out

out = np.any(SparseArray(data, fill_value=pos))
assert not out

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.any(SparseArray(data), out=out)
