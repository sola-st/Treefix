# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
joined = merge(df, df2)
exp = merge(df, df2, on=["key1", "key2"])
tm.assert_frame_equal(joined, exp)
