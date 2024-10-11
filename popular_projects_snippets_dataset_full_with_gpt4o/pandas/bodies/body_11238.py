# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py

# GH 10063
# using a non-time-based grouper and a time-based grouper
# and specifying levels
df = DataFrame(
    {"A": 1},
    index=MultiIndex.from_product(
        [list("ab"), date_range("20130101", periods=80)], names=["one", "two"]
    ),
)
result = df.groupby(
    [Grouper(level="one"), Grouper(level="two", freq="M")]
).sum()
expected = DataFrame(
    {"A": [31, 28, 21, 31, 28, 21]},
    index=MultiIndex.from_product(
        [list("ab"), date_range("20130101", freq="M", periods=3)],
        names=["one", "two"],
    ),
)
tm.assert_frame_equal(result, expected)
