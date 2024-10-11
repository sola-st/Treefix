# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_reindex.py
# GH#11586
msg = "cannot reindex on an axis with duplicate labels"
ci = CategoricalIndex(["a", "b", "c", "a"])
with pytest.raises(ValueError, match=msg):
    ci.reindex(["a", "c"])
