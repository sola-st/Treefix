# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
index = MultiIndex(
    levels=[Index(np.arange(4)), Index(np.arange(4)), Index(np.arange(4))],
    codes=[
        np.array([0, 0, 1, 2, 2, 2, 3, 3]),
        np.array([0, 1, 0, 0, 0, 1, 0, 1]),
        np.array([1, 0, 1, 1, 0, 0, 1, 0]),
    ],
)
msg = "[Kk]ey length.*greater than MultiIndex lexsort depth"
with pytest.raises(KeyError, match=msg):
    index.slice_locs((1, 0, 1), (2, 1, 0))

# works
sorted_index, _ = index.sortlevel(0)
# should there be a test case here???
sorted_index.slice_locs((1, 0, 1), (2, 1, 0))
