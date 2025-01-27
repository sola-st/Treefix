# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 24212
# pd.merge gets [0, 1, 2, -1, -1, -1] as left_indexer, ensure that
# -1 is interpreted as a missing value instead of the last element
df1 = DataFrame({"a": [0, 1, 2], "key": [0, 1, 2]}, index=index)
df2 = DataFrame({"b": [0, 1, 2, 3, 4, 5]})
result = df1.merge(df2, left_on="key", right_index=True, how=how)
expected = DataFrame(
    [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2],
        [np.nan, 3, 3],
        [np.nan, 4, 4],
        [np.nan, 5, 5],
    ],
    columns=["a", "key", "b"],
)
expected.set_index(expected_index, inplace=True)
tm.assert_frame_equal(result, expected)
