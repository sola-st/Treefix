# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#50467
df = DataFrame([["1", np.nan], ["2", np.nan], ["3", np.nan]], dtype=object)
rhs = DataFrame([[1, np.nan], [2, np.nan]])
indexer(df)[:idx, :] = rhs
expected = DataFrame([[1, np.nan], [2, np.nan], ["3", np.nan]], dtype=object)
tm.assert_frame_equal(df, expected)
