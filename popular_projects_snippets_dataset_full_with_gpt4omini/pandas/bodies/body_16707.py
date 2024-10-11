# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# Check if working name in df
df1, _ = dfs_for_indicator

for i in ["_right_indicator", "_left_indicator", "_merge"]:
    df_badcolumn = DataFrame({"col1": [1, 2], i: [2, 2]})

    msg = (
        "Cannot use `indicator=True` option when data contains a "
        f"column named {i}|"
        "Cannot use name of an existing column for indicator column"
    )
    with pytest.raises(ValueError, match=msg):
        merge(df1, df_badcolumn, on="col1", how="outer", indicator=True)
    with pytest.raises(ValueError, match=msg):
        df1.merge(df_badcolumn, on="col1", how="outer", indicator=True)

        # Check for name conflict with custom name
df_badcolumn = DataFrame({"col1": [1, 2], "custom_column_name": [2, 2]})

msg = "Cannot use name of an existing column for indicator column"
with pytest.raises(ValueError, match=msg):
    merge(
        df1,
        df_badcolumn,
        on="col1",
        how="outer",
        indicator="custom_column_name",
    )
with pytest.raises(ValueError, match=msg):
    df1.merge(
        df_badcolumn, on="col1", how="outer", indicator="custom_column_name"
    )
