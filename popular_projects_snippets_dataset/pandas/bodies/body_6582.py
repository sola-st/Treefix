# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_indexing.py
index = Index(["a", "a", "b", "c", "d", "d"])
assert index.slice_locs("a", "d") == (0, 6)
assert index.slice_locs(end="d") == (0, 6)
assert index.slice_locs("a", "c") == (0, 4)
assert index.slice_locs("b", "d") == (2, 6)

index2 = index[::-1]
assert index2.slice_locs("d", "a") == (0, 6)
assert index2.slice_locs(end="a") == (0, 6)
assert index2.slice_locs("d", "b") == (0, 4)
assert index2.slice_locs("c", "a") == (2, 6)
