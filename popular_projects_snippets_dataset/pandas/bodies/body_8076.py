# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
with pytest.raises(KeyError, match=""):
    index.drop(keys)
