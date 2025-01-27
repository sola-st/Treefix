# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH 6345
expected = DataFrame([[1 + 1j, 2], [np.nan, 4 + 1j]], columns=["a", "b"])
df = DataFrame([[1 + 1j, 2], [5 + 1j, 4 + 1j]], columns=["a", "b"])
df[df.abs() >= 5] = np.nan
tm.assert_frame_equal(df, expected)
