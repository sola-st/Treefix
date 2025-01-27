# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
df = DataFrame()
tm.assert_index_equal(df.columns, pd.RangeIndex(0))
df2 = DataFrame()
df2[1] = Series([1], index=["foo"])
df.loc[:, 1] = Series([1], index=["foo"])
tm.assert_frame_equal(df, DataFrame([[1]], index=["foo"], columns=[1]))
tm.assert_frame_equal(df, df2)
