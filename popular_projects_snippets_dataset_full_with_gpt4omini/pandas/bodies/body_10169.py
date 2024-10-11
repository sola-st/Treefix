# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 35869
df = DataFrame(
    {
        "column1": range(6),
        "column2": range(6),
        "group": 3 * ["A", "B"],
        "date": date_range(end="20190101", periods=6),
    }
)
result = (
    df.groupby("group")
    .rolling("3d", on="date", closed="left")["column1"]
    .count()
)
expected = Series(
    [np.nan, 1.0, 1.0, np.nan, 1.0, 1.0],
    name="column1",
    index=MultiIndex.from_tuples(
        [
            ("A", Timestamp("2018-12-27")),
            ("A", Timestamp("2018-12-29")),
            ("A", Timestamp("2018-12-31")),
            ("B", Timestamp("2018-12-28")),
            ("B", Timestamp("2018-12-30")),
            ("B", Timestamp("2019-01-01")),
        ],
        names=["group", "date"],
    ),
)
tm.assert_series_equal(result, expected)
