# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# issue 19132
idx = MultiIndex.from_arrays(index_arr)
result = idx.slice_indexer(start=start_idx, end=end_idx)
assert result == expected
