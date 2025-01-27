# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py

# increasing non-overlapping
index = IntervalIndex.from_tuples([(0, 1), (1, 2), (3, 4)])

assert index.slice_locs(0, 1) == (0, 1)
assert index.slice_locs(0, 2) == (0, 2)
assert index.slice_locs(0, 3) == (0, 2)
assert index.slice_locs(3, 1) == (2, 1)
assert index.slice_locs(3, 4) == (2, 3)
assert index.slice_locs(0, 4) == (0, 3)

# decreasing non-overlapping
index = IntervalIndex.from_tuples([(3, 4), (1, 2), (0, 1)])
assert index.slice_locs(0, 1) == (3, 3)
assert index.slice_locs(0, 2) == (3, 2)
assert index.slice_locs(0, 3) == (3, 1)
assert index.slice_locs(3, 1) == (1, 3)
assert index.slice_locs(3, 4) == (1, 1)
assert index.slice_locs(0, 4) == (3, 1)
