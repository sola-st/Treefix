# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index(np.array([0, 1, 2, 5, 6, 7, 9, 10], dtype=dtype))
n = len(index)

assert index.slice_locs(start=2) == (2, n)
assert index.slice_locs(start=3) == (3, n)
assert index.slice_locs(3, 8) == (3, 6)
assert index.slice_locs(5, 10) == (3, n)
assert index.slice_locs(end=8) == (0, 6)
assert index.slice_locs(end=9) == (0, 7)

# reversed
index2 = index[::-1]
assert index2.slice_locs(8, 2) == (2, 6)
assert index2.slice_locs(7, 3) == (2, 5)
