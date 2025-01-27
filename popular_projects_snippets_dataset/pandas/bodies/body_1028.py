# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_partial.py
# GH: 25165
date_idx = date_range("2019", periods=2, freq="MS")
df = DataFrame(
    list(range(4)),
    index=MultiIndex.from_product([date_idx, [0, 1]], names=["x", "y"]),
)
expected = DataFrame(
    exp_values,
    index=MultiIndex.from_product([exp_idx, [0, 1]], names=["x", "y"]),
)
result = df[indexer]
tm.assert_frame_equal(result, expected)
result = df.loc[indexer]
tm.assert_frame_equal(result, expected)

result = df.loc(axis=0)[indexer]
tm.assert_frame_equal(result, expected)

result = df.loc[indexer, :]
tm.assert_frame_equal(result, expected)

df2 = df.swaplevel(0, 1).sort_index()
expected = expected.swaplevel(0, 1).sort_index()

result = df2.loc[:, indexer, :]
tm.assert_frame_equal(result, expected)
