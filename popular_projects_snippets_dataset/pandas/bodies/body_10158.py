# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 37141
df = DataFrame(
    data={
        "Date": date_range("2020-01-01", "2020-01-10"),
        "gb": ["group_1"] * 6 + ["group_2"] * 4,
        "value": range(10),
    }
)
result = (
    df.groupby("gb")
    .rolling(6, on="Date", center=True, min_periods=1)
    .value.mean()
)
expected = Series(
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 7.0, 7.5, 7.5, 7.5],
    name="value",
    index=MultiIndex.from_tuples(
        (
            ("group_1", Timestamp("2020-01-01")),
            ("group_1", Timestamp("2020-01-02")),
            ("group_1", Timestamp("2020-01-03")),
            ("group_1", Timestamp("2020-01-04")),
            ("group_1", Timestamp("2020-01-05")),
            ("group_1", Timestamp("2020-01-06")),
            ("group_2", Timestamp("2020-01-07")),
            ("group_2", Timestamp("2020-01-08")),
            ("group_2", Timestamp("2020-01-09")),
            ("group_2", Timestamp("2020-01-10")),
        ),
        names=["gb", "Date"],
    ),
)
tm.assert_series_equal(result, expected)
