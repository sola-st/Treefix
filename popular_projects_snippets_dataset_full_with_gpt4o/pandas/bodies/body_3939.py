# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 18303 - wrong level name should raise
frame = multiindex_dataframe_random_data

# A DataFrame with flat axes:
df = frame.loc["foo"]

with pytest.raises(KeyError, match="does not match index name"):
    getattr(df, method)("mistake")

if method == "unstack":
    # Same on a Series:
    s = df.iloc[:, 0]
    with pytest.raises(KeyError, match="does not match index name"):
        getattr(s, method)("mistake")
