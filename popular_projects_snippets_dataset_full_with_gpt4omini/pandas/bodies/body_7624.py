# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#19027
# test that dropped MultiIndex levels are not in the MultiIndex
# despite continuing to be in the MultiIndex's levels
idx = MultiIndex.from_product([[1, 2], [3, 4]])
assert 2 in idx
idx = idx.drop(2)

# drop implementation keeps 2 in the levels
assert 2 in idx.levels[0]
# but it should no longer be in the index itself
assert 2 not in idx

# also applies to strings
idx = MultiIndex.from_product([["a", "b"], ["c", "d"]])
assert "a" in idx
idx = idx.drop("a")
assert "a" in idx.levels[0]
assert "a" not in idx
