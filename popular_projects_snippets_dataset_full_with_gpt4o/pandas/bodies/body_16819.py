# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# no overlapping blocks
df1 = DataFrame(index=np.arange(10))
df1["bool"] = True
df1["string"] = "foo"

df2 = DataFrame(index=np.arange(5, 15))
df2["int"] = 1
df2["float"] = 1.0

joined = df1.join(df2, how=join_type)
expected = _join_by_hand(df1, df2, how=join_type)
tm.assert_frame_equal(joined, expected)

joined = df2.join(df1, how=join_type)
expected = _join_by_hand(df2, df1, how=join_type)
tm.assert_frame_equal(joined, expected)
