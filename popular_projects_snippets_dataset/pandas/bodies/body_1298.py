# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
with pytest.raises(KeyError, match="^1$"):
    df.loc[1]
