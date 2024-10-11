# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# not all labels in the categories
with pytest.raises(KeyError, match=re.escape("['d'] not in index")):
    df2.loc[["a", "d"]]
