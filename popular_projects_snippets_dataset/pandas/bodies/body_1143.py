# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#31330
df = DataFrame(
    [[1, 2], [3, 4], [5, 6], [7, 8]],
    index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
    columns=["a", "b"],
)
result = df.loc[(slice(None), [2, 1]), :]
expected = DataFrame(
    [[3, 4], [7, 8], [1, 2], [5, 6]],
    index=[["a", "b", "a", "b"], [2, 2, 1, 1]],
    columns=["a", "b"],
)
tm.assert_frame_equal(result, expected)
