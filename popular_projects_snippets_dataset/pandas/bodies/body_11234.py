# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py

# GH 8795
df = DataFrame({"A": [0, 0, 1, 1, 2, 2], "B": [1, 2, 3, 4, 5, 6]})
g = df.groupby("A")
expected = g.sum()

g = df.groupby(Grouper(key="A"))
result = g.sum()
tm.assert_frame_equal(result, expected)

g = df.groupby(Grouper(key="A", axis=0))
result = g.sum()
tm.assert_frame_equal(result, expected)

result = g.apply(lambda x: x.sum())
expected["A"] = [0, 2, 4]
expected = expected.loc[:, ["A", "B"]]
tm.assert_frame_equal(result, expected)

# GH14334
# Grouper(key=...) may be passed in a list
df = DataFrame(
    {"A": [0, 0, 0, 1, 1, 1], "B": [1, 1, 2, 2, 3, 3], "C": [1, 2, 3, 4, 5, 6]}
)
# Group by single column
expected = df.groupby("A").sum()
g = df.groupby([Grouper(key="A")])
result = g.sum()
tm.assert_frame_equal(result, expected)

# Group by two columns
# using a combination of strings and Grouper objects
expected = df.groupby(["A", "B"]).sum()

# Group with two Grouper objects
g = df.groupby([Grouper(key="A"), Grouper(key="B")])
result = g.sum()
tm.assert_frame_equal(result, expected)

# Group with a string and a Grouper object
g = df.groupby(["A", Grouper(key="B")])
result = g.sum()
tm.assert_frame_equal(result, expected)

# Group with a Grouper object and a string
g = df.groupby([Grouper(key="A"), "B"])
result = g.sum()
tm.assert_frame_equal(result, expected)

# GH8866
s = Series(
    np.arange(8, dtype="int64"),
    index=MultiIndex.from_product(
        [list("ab"), range(2), date_range("20130101", periods=2)],
        names=["one", "two", "three"],
    ),
)
result = s.groupby(Grouper(level="three", freq="M")).sum()
expected = Series(
    [28],
    index=pd.DatetimeIndex([Timestamp("2013-01-31")], freq="M", name="three"),
)
tm.assert_series_equal(result, expected)

# just specifying a level breaks
result = s.groupby(Grouper(level="one")).sum()
expected = s.groupby(level="one").sum()
tm.assert_series_equal(result, expected)
