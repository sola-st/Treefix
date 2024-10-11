# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
idx1 = MultiIndex.from_product([["a", "b"], [1, 2]])
idx2 = MultiIndex.from_product([["b", "c"], [1, 2]])

with pytest.raises(ValueError, match="The 'sort' keyword only takes"):
    getattr(idx1, method)(idx2, sort=True)
