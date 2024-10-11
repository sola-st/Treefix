# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
sorted_idx, _ = idx.sortlevel(0)
assert sorted_idx.get_loc("baz") == slice(3, 4)
assert sorted_idx.get_loc("foo") == slice(0, 2)
