# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = simple_index
with pytest.raises(TypeError, match="'>|<' not supported"):
    index.argsort()
