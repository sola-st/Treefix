# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index([1, 2, 3])
with pytest.raises(KeyError, match=""):
    index.drop([3, 4])
