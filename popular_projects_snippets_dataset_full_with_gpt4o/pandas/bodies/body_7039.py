# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
# GH#21729
idx = CategoricalIndex([1, 2, 3])

assert "a" not in idx

with pytest.raises(TypeError, match="unhashable type"):
    ["a"] in idx

with pytest.raises(TypeError, match="unhashable type"):
    ["a", "b"] in idx
