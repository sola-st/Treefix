# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# GH#37901 a label that is in index.categories but not in index
# listlike containing an element in the categories but not in the values
with pytest.raises(KeyError, match=re.escape("['e'] not in index")):
    df2.loc[["a", "b", "e"]]
