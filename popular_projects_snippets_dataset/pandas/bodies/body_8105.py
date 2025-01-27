# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(list("ABC"), name="xxx")
with pytest.raises(IndexError, match="out of bounds"):
    index.take(np.array([1, -5]))
