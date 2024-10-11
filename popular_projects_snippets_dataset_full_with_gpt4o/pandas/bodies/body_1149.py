# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 16018
result = DataFrame(
    [[1, 2, 5, 6], [3, 4, 7, 8]],
    index=["a", "a"],
    columns=MultiIndex.from_product([[1, 2], ["A", "B"]]),
)
result.loc["c"] = -1
result.loc["c", (1, "A")] = 3
result.loc["d", (1, "A")] = 3
expected = DataFrame(
    [
        [1.0, 2.0, 5.0, 6.0],
        [3.0, 4.0, 7.0, 8.0],
        [3.0, -1.0, -1, -1],
        [3.0, np.nan, np.nan, np.nan],
    ],
    index=["a", "a", "c", "d"],
    columns=MultiIndex.from_product([[1, 2], ["A", "B"]]),
)
tm.assert_frame_equal(result, expected)
