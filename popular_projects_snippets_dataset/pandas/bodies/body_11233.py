# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 7885
# with level and freq specified in a Grouper
d0 = date.today() - timedelta(days=14)
dates = date_range(d0, date.today())
date_index = MultiIndex.from_product([dates, dates], names=["foo", "bar"])
df = DataFrame(np.random.randint(0, 100, 225), index=date_index)

# Check string level
expected = (
    df.reset_index()
    .groupby([Grouper(key="foo", freq="W"), Grouper(key="bar", freq="W")])
    .sum()
)
# reset index changes columns dtype to object
expected.columns = Index([0], dtype="int64")

result = df.groupby(
    [Grouper(level="foo", freq="W"), Grouper(level="bar", freq="W")]
).sum()
tm.assert_frame_equal(result, expected)

# Check integer level
result = df.groupby(
    [Grouper(level=0, freq="W"), Grouper(level=1, freq="W")]
).sum()
tm.assert_frame_equal(result, expected)
