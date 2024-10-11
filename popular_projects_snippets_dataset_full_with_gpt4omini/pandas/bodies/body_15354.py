# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# integer indexes, be careful
ser = Series(np.random.randn(10), index=list(range(0, 20, 2)))
inds = [0, 2, 5, 7, 8]
arr_inds = np.array([0, 2, 5, 7, 8])
with pytest.raises(KeyError, match="not in index"):
    ser[inds]

with pytest.raises(KeyError, match="not in index"):
    ser[arr_inds]
