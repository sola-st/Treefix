# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# Accessing a Category that is not in the dataframe
df = DataFrame({"var": ["a", "a", "b", "b"], "val": range(4)})
with pytest.raises(KeyError, match="'vau'"):
    df.groupby("var").apply(
        lambda rows: DataFrame(
            {"var": [rows.iloc[-1]["var"]], "val": [rows.iloc[-1]["vau"]]}
        )
    )
