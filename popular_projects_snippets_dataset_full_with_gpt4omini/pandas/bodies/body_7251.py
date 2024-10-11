# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index([np.nan, 1, 2])
with pytest.raises(KeyError, match=""):
    index.slice_locs(start=1.5)

with pytest.raises(KeyError, match=""):
    index.slice_locs(end=1.5)
