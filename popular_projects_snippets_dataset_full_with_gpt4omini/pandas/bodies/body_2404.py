# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# dtype changing GH4204
df = DataFrame([[0, 0]])
df.iloc[0] = np.nan
expected = DataFrame([[np.nan, np.nan]])
tm.assert_frame_equal(df, expected)

df = DataFrame([[0, 0]])
df.loc[0] = np.nan
tm.assert_frame_equal(df, expected)
