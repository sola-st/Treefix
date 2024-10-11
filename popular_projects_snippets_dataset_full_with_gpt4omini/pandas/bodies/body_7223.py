# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# unique but non-monotonic goes through IndexEngine.mapping.get_item
idx = Index([0, 2, 1])

val = np.iinfo(np.int64).max + 1

with pytest.raises(KeyError, match=str(val)):
    idx.get_loc(val)
with pytest.raises(KeyError, match=str(val)):
    idx._engine.get_loc(val)
