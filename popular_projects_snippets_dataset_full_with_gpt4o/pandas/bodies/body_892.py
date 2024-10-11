# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
idx = Index([0, 1, 2, 3, 4])
a = Series([1, 2, 3]).reindex(idx)
b = Series(Categorical([1, 2, 3])).reindex(idx)

assert a._mgr.blocks[0].mgr_locs.indexer == b._mgr.blocks[0].mgr_locs.indexer
