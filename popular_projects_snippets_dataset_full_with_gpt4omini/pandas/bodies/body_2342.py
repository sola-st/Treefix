# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH 31687
df = DataFrame([[1.0, 2e25, "nine"], [np.nan, 0.1, None]])
result = df.where(pd.notnull(df), replacement)
expected = DataFrame([[1.0, 2e25, "nine"], [replacement, 0.1, replacement]])

tm.assert_frame_equal(result, expected)
