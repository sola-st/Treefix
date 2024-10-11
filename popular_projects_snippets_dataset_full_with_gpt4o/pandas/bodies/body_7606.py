# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
index = Index([2, 2, 2, 2])
result = index.get_loc(2)
expected = slice(0, 4)
assert result == expected

index = Index(["c", "a", "a", "b", "b"])
rs = index.get_loc("c")
xp = 0
assert rs == xp

with pytest.raises(KeyError, match="2"):
    index.get_loc(2)
