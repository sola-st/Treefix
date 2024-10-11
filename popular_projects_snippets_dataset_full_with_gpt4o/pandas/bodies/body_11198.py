# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH #42395
df = DataFrame(
    {
        "x": [1, 0, 1, 1, 0],
        "y": [Timedelta(i, "days") for i in range(1, 6)],
        "z": [Timedelta(i * 10, "days") for i in range(1, 6)],
    }
)

expected = DataFrame(
    {
        "y": [Timedelta(i, "days") for i in range(7, 9)],
        "z": [Timedelta(i * 10, "days") for i in range(7, 9)],
    },
    index=Index([0, 1], dtype="int64", name="x"),
)

gb = df.groupby(by=["x"])
result = gb.sum()
tm.assert_frame_equal(result, expected)
