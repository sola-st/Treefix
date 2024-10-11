# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# see GH#10126
kwargs["dtype"] = dtype
df = DataFrame(**kwargs)

df2 = df.copy()
df[df > df2] = 47
tm.assert_frame_equal(df, df2)
