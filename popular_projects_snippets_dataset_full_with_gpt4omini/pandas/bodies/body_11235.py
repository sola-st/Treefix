# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 14327

# Grouping a multi-index frame by a column and an index level should
# be equivalent to resetting the index and grouping by two columns
idx = MultiIndex.from_tuples(
    [("a", 1), ("a", 2), ("a", 3), ("b", 1), ("b", 2), ("b", 3)]
)
idx.names = ["outer", "inner"]
df_multi = DataFrame(
    {"A": np.arange(6), "B": ["one", "one", "two", "two", "one", "one"]},
    index=idx,
)
result = df_multi.groupby(["B", Grouper(level="inner")]).mean(numeric_only=True)
expected = (
    df_multi.reset_index().groupby(["B", "inner"]).mean(numeric_only=True)
)
tm.assert_frame_equal(result, expected)

# Test the reverse grouping order
result = df_multi.groupby([Grouper(level="inner"), "B"]).mean(numeric_only=True)
expected = (
    df_multi.reset_index().groupby(["inner", "B"]).mean(numeric_only=True)
)
tm.assert_frame_equal(result, expected)

# Grouping a single-index frame by a column and the index should
# be equivalent to resetting the index and grouping by two columns
df_single = df_multi.reset_index("outer")
result = df_single.groupby(["B", Grouper(level="inner")]).mean(
    numeric_only=True
)
expected = (
    df_single.reset_index().groupby(["B", "inner"]).mean(numeric_only=True)
)
tm.assert_frame_equal(result, expected)

# Test the reverse grouping order
result = df_single.groupby([Grouper(level="inner"), "B"]).mean(
    numeric_only=True
)
expected = (
    df_single.reset_index().groupby(["inner", "B"]).mean(numeric_only=True)
)
tm.assert_frame_equal(result, expected)
