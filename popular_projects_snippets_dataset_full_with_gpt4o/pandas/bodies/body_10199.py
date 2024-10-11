# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 43355
df = DataFrame(
    {
        "id": ["a", "a", "b", "b", "b"],
        "timestamp": date_range("2021-9-1", periods=5, freq="H"),
        "y": range(5),
    }
)
grp = df.groupby("id").rolling("1H", on="timestamp")
result = grp.count()
expected_df = DataFrame(
    {
        "timestamp": date_range("2021-9-1", periods=5, freq="H"),
        "y": [1.0] * 5,
    },
    index=MultiIndex.from_arrays(
        [["a", "a", "b", "b", "b"], list(range(5))], names=["id", None]
    ),
)
tm.assert_frame_equal(result, expected_df)

result = grp["y"].count()
expected_series = Series(
    [1.0] * 5,
    index=MultiIndex.from_arrays(
        [
            ["a", "a", "b", "b", "b"],
            date_range("2021-9-1", periods=5, freq="H"),
        ],
        names=["id", "timestamp"],
    ),
    name="y",
)
tm.assert_series_equal(result, expected_series)
# This is the key test
result = grp.count()
tm.assert_frame_equal(result, expected_df)
