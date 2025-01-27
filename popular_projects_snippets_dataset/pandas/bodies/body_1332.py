# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

df1 = DataFrame(np.random.randn(10, 4), columns=["A", "A", "B", "B"])
df2 = DataFrame(
    np.random.randint(0, 10, size=20).reshape(10, 2), columns=["A", "C"]
)

# axis=1
df = concat([df1, df2], axis=1)
tm.assert_frame_equal(df.iloc[:, :4], df1)
tm.assert_frame_equal(df.iloc[:, 4:], df2)

df = concat([df2, df1], axis=1)
tm.assert_frame_equal(df.iloc[:, :2], df2)
tm.assert_frame_equal(df.iloc[:, 2:], df1)

exp = concat([df2, df1.iloc[:, [0]]], axis=1)
tm.assert_frame_equal(df.iloc[:, 0:3], exp)

# axis=0
df = concat([df, df], axis=0)
tm.assert_frame_equal(df.iloc[0:10, :2], df2)
tm.assert_frame_equal(df.iloc[0:10, 2:], df1)
tm.assert_frame_equal(df.iloc[10:, :2], df2)
tm.assert_frame_equal(df.iloc[10:, 2:], df1)
