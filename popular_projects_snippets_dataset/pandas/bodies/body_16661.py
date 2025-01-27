# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH14355

left = df.set_index("key1")
right = df2.set_index("key1")
result = merge(left, right, on="key1")
expected = merge(df, df2, on="key1").set_index("key1")
tm.assert_frame_equal(result, expected)
