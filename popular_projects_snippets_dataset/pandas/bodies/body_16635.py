# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH 27642

left = pd.DataFrame(
    list(zip([0, 5, 10, 15, 20, 25], [0, 1, 2, 3, 4, 5])),
    columns=["time", "left"],
)

left["time"] = pd.to_timedelta(left["time"], "ms")

right = pd.DataFrame(
    list(zip([0, 3, 9, 12, 15, 18], [0, 1, 2, 3, 4, 5])),
    columns=["time", "right"],
)

right["time"] = pd.to_timedelta(right["time"], "ms")

expected = pd.DataFrame(
    list(
        zip(
            [0, 5, 10, 15, 20, 25],
            [0, 1, 2, 3, 4, 5],
            [0, np.nan, 2, 4, np.nan, np.nan],
        )
    ),
    columns=["time", "left", "right"],
)

expected["time"] = pd.to_timedelta(expected["time"], "ms")

result = merge_asof(
    left, right, on="time", tolerance=Timedelta("1ms"), direction="nearest"
)

tm.assert_frame_equal(result, expected)
