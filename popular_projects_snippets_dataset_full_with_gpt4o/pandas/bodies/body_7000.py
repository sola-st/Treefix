# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_reindex.py
msg = "cannot reindex on an axis with duplicate labels"
ci = CategoricalIndex(["a", "b", "c", "a"], categories=["a", "b", "c", "d"])
with pytest.raises(ValueError, match=msg):
    ci.reindex(["a", "c"])
