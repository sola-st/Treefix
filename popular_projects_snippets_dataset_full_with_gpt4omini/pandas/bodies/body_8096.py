# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
with pytest.raises(AttributeError, match="only use .str accessor"):
    index.str.repeat(2)
