# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
df = DataFrame(
    np.random.randn(3, 3), index=[0.1, 0.2, 0.2], columns=list("abc")
)
expect = df.iloc[1:]
tm.assert_frame_equal(df.loc[0.2], expect)

expect = df.iloc[1:, 0]
tm.assert_series_equal(df.loc[0.2, "a"], expect)

df.index = [1, 0.2, 0.2]
expect = df.iloc[1:]
tm.assert_frame_equal(df.loc[0.2], expect)

expect = df.iloc[1:, 0]
tm.assert_series_equal(df.loc[0.2, "a"], expect)

df = DataFrame(
    np.random.randn(4, 3), index=[1, 0.2, 0.2, 1], columns=list("abc")
)
expect = df.iloc[1:-1]
tm.assert_frame_equal(df.loc[0.2], expect)

expect = df.iloc[1:-1, 0]
tm.assert_series_equal(df.loc[0.2, "a"], expect)

df.index = [0.1, 0.2, 2, 0.2]
expect = df.iloc[[1, -1]]
tm.assert_frame_equal(df.loc[0.2], expect)

expect = df.iloc[[1, -1], 0]
tm.assert_series_equal(df.loc[0.2, "a"], expect)
