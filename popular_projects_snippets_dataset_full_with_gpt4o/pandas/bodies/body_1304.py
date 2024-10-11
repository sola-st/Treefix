# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# element in the categories but not in the values
with pytest.raises(KeyError, match=r"^'e'$"):
    df2.loc["e"]
