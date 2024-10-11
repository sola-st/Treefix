# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# issue 19132
idx = MultiIndex.from_arrays(index_arr)
result = idx.get_slice_bound(target, side=algo)
assert result == expected
