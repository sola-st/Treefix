# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
idx = Index([np.nan, 1, 2], dtype=np.float64)
assert idx.get_loc(1) == 1
assert idx.get_loc(np.nan) == 0

idx = Index([np.nan, 1, np.nan], dtype=np.float64)
assert idx.get_loc(1) == 1

# representable by slice [0:2:2]
msg = "'Cannot get left slice bound for non-unique label: nan'"
with pytest.raises(KeyError, match=msg):
    idx.slice_locs(np.nan)
# not representable by slice
idx = Index([np.nan, 1, np.nan, np.nan], dtype=np.float64)
assert idx.get_loc(1) == 1
msg = "'Cannot get left slice bound for non-unique label: nan"
with pytest.raises(KeyError, match=msg):
    idx.slice_locs(np.nan)
