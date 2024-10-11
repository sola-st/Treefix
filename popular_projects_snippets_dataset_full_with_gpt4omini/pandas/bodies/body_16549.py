# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
left = DataFrame(
    [
        ["X", "Y", "C", "a"],
        ["W", "Y", "C", "e"],
        ["V", "Q", "A", "h"],
        ["V", "R", "D", "i"],
        ["X", "Y", "D", "b"],
        ["X", "Y", "A", "c"],
        ["W", "Q", "B", "f"],
        ["W", "R", "C", "g"],
        ["V", "Y", "C", "j"],
        ["X", "Y", "B", "d"],
    ],
    columns=["cola", "colb", "colc", "tag"],
    index=[3, 2, 0, 1, 7, 6, 4, 5, 9, 8],
)

right = DataFrame(
    [
        ["W", "R", "C", 0],
        ["W", "Q", "B", 3],
        ["W", "Q", "B", 8],
        ["X", "Y", "A", 1],
        ["X", "Y", "A", 4],
        ["X", "Y", "B", 5],
        ["X", "Y", "C", 6],
        ["X", "Y", "C", 9],
        ["X", "Q", "C", -6],
        ["X", "R", "C", -9],
        ["V", "Y", "C", 7],
        ["V", "R", "D", 2],
        ["V", "R", "D", -1],
        ["V", "Q", "A", -3],
    ],
    columns=["col1", "col2", "col3", "val"],
).set_index(["col1", "col2", "col3"])

result = left.join(right, on=["cola", "colb", "colc"], how="left")

expected = DataFrame(
    [
        ["X", "Y", "C", "a", 6],
        ["X", "Y", "C", "a", 9],
        ["W", "Y", "C", "e", np.nan],
        ["V", "Q", "A", "h", -3],
        ["V", "R", "D", "i", 2],
        ["V", "R", "D", "i", -1],
        ["X", "Y", "D", "b", np.nan],
        ["X", "Y", "A", "c", 1],
        ["X", "Y", "A", "c", 4],
        ["W", "Q", "B", "f", 3],
        ["W", "Q", "B", "f", 8],
        ["W", "R", "C", "g", 0],
        ["V", "Y", "C", "j", 7],
        ["X", "Y", "B", "d", 5],
    ],
    columns=["cola", "colb", "colc", "tag", "val"],
    index=[3, 3, 2, 0, 1, 1, 7, 6, 6, 4, 4, 5, 9, 8],
)

tm.assert_frame_equal(result, expected)

result = left.join(right, on=["cola", "colb", "colc"], how="left", sort=True)

expected = expected.sort_values(["cola", "colb", "colc"], kind="mergesort")

tm.assert_frame_equal(result, expected)
