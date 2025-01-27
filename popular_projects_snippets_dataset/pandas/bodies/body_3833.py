# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
df = DataFrame([[1, 2, "foo", "bar"]], columns=["a", "a", "a", "a"])
df.columns = ["a", "a.1", "a.2", "a.3"]
str(df)
expected = DataFrame([[1, 2, "foo", "bar"]], columns=["a", "a.1", "a.2", "a.3"])
tm.assert_frame_equal(df, expected)
