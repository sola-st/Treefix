# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 35549
df = DataFrame(
    {
        "column1": range(6),
        "column2": range(6),
        "group": 3 * ["A", "B"],
        "date": [Timestamp("2019-01-01")] * 6,
    }
)
result = (
    df.groupby("group").rolling("1D", on="date", closed="left")["column1"].sum()
)
expected = Series(
    [np.nan, 0.0, 2.0, np.nan, 1.0, 4.0],
    index=MultiIndex.from_tuples(
        [("A", Timestamp("2019-01-01"))] * 3
        + [("B", Timestamp("2019-01-01"))] * 3,
        names=["group", "date"],
    ),
    name="column1",
)
tm.assert_series_equal(result, expected)
