# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
idx1 = Index(["a", "b"])
idx2 = Index(["b", "c"])

with pytest.raises(ValueError, match="The 'sort' keyword only takes"):
    getattr(idx1, method)(idx2, sort=True)
