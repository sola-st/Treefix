# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

# using multiple aggregation columns
df = DataFrame(
    {
        "A": [0, 1, 2, 3, 4],
        "B": [0, 1, 2, np.nan, 4],
        "C": Index(
            [
                Timestamp("20130101 09:00:00"),
                Timestamp("20130101 09:00:02"),
                Timestamp("20130101 09:00:03"),
                Timestamp("20130101 09:00:05"),
                Timestamp("20130101 09:00:06"),
            ]
        ),
    },
    columns=["A", "C", "B"],
)

expected1 = DataFrame(
    {"A": [0.0, 1, 3, 3, 7], "B": [0, 1, 3, np.nan, 4], "C": df["C"]},
    columns=["A", "C", "B"],
)

result = df.rolling("2s", on="C").sum()
expected = expected1
tm.assert_frame_equal(result, expected)

expected = Series([0, 1, 3, np.nan, 4], name="B")
result = df.rolling("2s", on="C").B.sum()
tm.assert_series_equal(result, expected)

expected = expected1[["A", "B", "C"]]
result = df.rolling("2s", on="C")[["A", "B", "C"]].sum()
tm.assert_frame_equal(result, expected)
