# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# key that is an *unused* category raises
index = CategoricalIndex(["a", "b", "a", "c"], categories=list("abcde"))
df = DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]}, index=index)

with pytest.raises(KeyError, match="e"):
    # For comparison, check the scalar behavior
    df.loc["e"]

with pytest.raises(KeyError, match=re.escape("['e'] not in index")):
    df.loc[["a", "e"]]
