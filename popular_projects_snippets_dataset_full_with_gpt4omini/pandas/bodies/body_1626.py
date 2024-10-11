# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#4125
idx = pd.period_range("2002-01", "2003-12", freq="M")
df = DataFrame(np.random.randn(24, 10), index=idx)
tm.assert_frame_equal(df, df.loc[idx])
tm.assert_frame_equal(df, df.loc[list(idx)])
tm.assert_frame_equal(df, df.loc[list(idx)])
tm.assert_frame_equal(df.iloc[0:5], df.loc[idx[0:5]])
tm.assert_frame_equal(df, df.loc[list(idx)])
