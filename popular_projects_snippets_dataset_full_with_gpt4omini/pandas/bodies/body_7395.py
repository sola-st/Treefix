# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_sorting.py
# GH 37510
idx = Index([(1, np.nan), (3, 4)]).rename(["id1", "id2"])
idx = idx.set_levels(["a", np.nan], level="id1")
idx = idx.remove_unused_levels()
result = idx.levels
expected = FrozenList([["a", np.nan], [4]])
assert str(result) == str(expected)
