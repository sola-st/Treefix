# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH45032
df = DataFrame([[6, "c", 10], [7, "d", 11], [8, "e", 12]])
expected = DataFrame([[6, "c", 10], [7, "d", 11], [5, 5, 5]])
df.iloc(axis=0)[2] = 5
tm.assert_frame_equal(df, expected)

df = DataFrame([[6, "c", 10], [7, "d", 11], [8, "e", 12]])
expected = DataFrame([[6, "c", 5], [7, "d", 5], [8, "e", 5]])
df.iloc(axis=1)[2] = 5
tm.assert_frame_equal(df, expected)
