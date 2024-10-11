# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# with a dup index
df = DataFrame([[1, 2]], columns=["a", "a"])
df.columns = ["b", "b"]
str(df)
expected = DataFrame([[1, 2]], columns=["b", "b"])
tm.assert_frame_equal(df, expected)
