# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# Check only accepts strings and booleans
df1, df2 = dfs_for_indicator

msg = "indicator option can only accept boolean or string arguments"
with pytest.raises(ValueError, match=msg):
    merge(df1, df2, on="col1", how="outer", indicator=5)
with pytest.raises(ValueError, match=msg):
    df1.merge(df2, on="col1", how="outer", indicator=5)
