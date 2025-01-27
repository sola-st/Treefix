# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# multi-dtype
df = DataFrame(
    [[1, 2, 1.0, 2.0, 3.0, "foo", "bar"]],
    columns=["a", "a", "b", "b", "d", "c", "c"],
)
df.columns = list("ABCDEFG")
str(df)
expected = DataFrame(
    [[1, 2, 1.0, 2.0, 3.0, "foo", "bar"]], columns=list("ABCDEFG")
)
tm.assert_frame_equal(df, expected)
