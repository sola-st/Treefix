# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index([1, 2, 3])
with pytest.raises(AttributeError, match="Can't set attribute"):
    index.is_unique = False
