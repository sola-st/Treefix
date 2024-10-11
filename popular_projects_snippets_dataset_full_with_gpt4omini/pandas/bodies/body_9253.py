# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# GH#21729
cat = Categorical([1, 2, 3])

assert "a" not in cat

with pytest.raises(TypeError, match="unhashable type"):
    ["a"] in cat

with pytest.raises(TypeError, match="unhashable type"):
    ["a", "b"] in cat
