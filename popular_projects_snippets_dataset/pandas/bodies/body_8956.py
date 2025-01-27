# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
# GH#17570
out = np.all(SparseArray(data))
assert out

out = np.all(SparseArray(data, fill_value=pos))
assert out

data[1] = neg
out = np.all(SparseArray(data))
assert not out

out = np.all(SparseArray(data, fill_value=pos))
assert not out

# raises with a different message on py2.
msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.all(SparseArray(data), out=np.array([]))
