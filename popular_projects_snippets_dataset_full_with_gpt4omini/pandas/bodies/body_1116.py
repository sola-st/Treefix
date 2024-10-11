# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#39147
mi = MultiIndex.from_tuples([(1, 2), (3, 4)])
df = DataFrame([[1, 2], [3, 4]], index=mi, columns=["a", "b"])
df.loc[indexer, ["c", "d"]] = 1.0
expected = DataFrame(
    [[1, 2, 1.0, 1.0], [3, 4, exp_value, exp_value]],
    index=mi,
    columns=["a", "b", "c", "d"],
)
tm.assert_frame_equal(df, expected)
