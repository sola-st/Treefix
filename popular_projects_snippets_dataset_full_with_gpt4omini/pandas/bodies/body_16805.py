# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
joined_key2 = merge(df, df2, on="key2", how="inner")
_check_join(df, df2, joined_key2, ["key2"], how="inner")

joined_both = merge(df, df2, how="inner")
_check_join(df, df2, joined_both, ["key1", "key2"], how="inner")
