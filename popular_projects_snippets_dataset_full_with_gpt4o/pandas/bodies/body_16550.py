# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
left = DataFrame(
    [["c", 0], ["b", 1], ["a", 2], ["b", 3]],
    columns=["tag", "val"],
    index=[2, 0, 1, 3],
)

right = DataFrame(
    [
        ["a", "v"],
        ["c", "w"],
        ["c", "x"],
        ["d", "y"],
        ["a", "z"],
        ["c", "r"],
        ["e", "q"],
        ["c", "s"],
    ],
    columns=["tag", "char"],
).set_index("tag")

result = left.join(right, on="tag", how="left")

expected = DataFrame(
    [
        ["c", 0, "w"],
        ["c", 0, "x"],
        ["c", 0, "r"],
        ["c", 0, "s"],
        ["b", 1, np.nan],
        ["a", 2, "v"],
        ["a", 2, "z"],
        ["b", 3, np.nan],
    ],
    columns=["tag", "val", "char"],
    index=[2, 2, 2, 2, 0, 1, 1, 3],
)

tm.assert_frame_equal(result, expected)

result = left.join(right, on="tag", how="left", sort=True)
expected2 = expected.sort_values("tag", kind="mergesort")

tm.assert_frame_equal(result, expected2)

# GH7331 - maintain left frame order in left merge
result = merge(left, right.reset_index(), how="left", on="tag")
expected.index = RangeIndex(len(expected))
tm.assert_frame_equal(result, expected)
