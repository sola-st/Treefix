# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# GH 3468 related

# basic
df = DataFrame([[1, 2]], columns=["a", "a"])
df.columns = ["a", "a.1"]
str(df)
expected = DataFrame([[1, 2]], columns=["a", "a.1"])
tm.assert_frame_equal(df, expected)

df = DataFrame([[1, 2, 3]], columns=["b", "a", "a"])
df.columns = ["b", "a", "a.1"]
str(df)
expected = DataFrame([[1, 2, 3]], columns=["b", "a", "a.1"])
tm.assert_frame_equal(df, expected)
