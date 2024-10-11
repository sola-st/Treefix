# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH 47362
df = DataFrame(
    data={
        "date": date_range(start="2016-01-01", periods=8),
        "group": [0, 0, 0, 0, 1, 1, 1, 1],
        "val": [1, 7, 5, 2, 3, 10, 5, 1],
    }
)
result = df.groupby("group").resample("2D", on="date")[["val"]].mean()
expected = DataFrame(
    data={
        "val": [4.0, 3.5, 6.5, 3.0],
    },
    index=Index(
        data=[
            (0, Timestamp("2016-01-01")),
            (0, Timestamp("2016-01-03")),
            (1, Timestamp("2016-01-05")),
            (1, Timestamp("2016-01-07")),
        ],
        name=("group", "date"),
    ),
)
tm.assert_frame_equal(result, expected)
