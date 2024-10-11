# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#14946
df = DataFrame({"x": range(10)})
df.index = to_timedelta(range(10), unit="s")
conditions = [df["x"] > 3, df["x"] == 3, df["x"] < 3]
expected_data = [
    [0, 1, 2, 3, 10, 10, 10, 10, 10, 10],
    [0, 1, 2, 10, 4, 5, 6, 7, 8, 9],
    [10, 10, 10, 3, 4, 5, 6, 7, 8, 9],
]
for cond, data in zip(conditions, expected_data):
    result = df.copy()
    result.loc[cond, "x"] = 10

    expected = DataFrame(
        data,
        index=to_timedelta(range(10), unit="s"),
        columns=["x"],
        dtype="int64",
    )
    tm.assert_frame_equal(expected, result)
