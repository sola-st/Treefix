# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH #16871
index = pd.period_range("2016-01-01", periods=16, freq="M")
df = DataFrame(list(range(len(index))), index=index, columns=["pnum"])
df2 = concat([df, df])
result = df.join(df2, how="inner", rsuffix="_df2")
expected = DataFrame(
    np.tile(np.arange(16, dtype=np.int64).repeat(2).reshape(-1, 1), 2),
    columns=["pnum", "pnum_df2"],
    index=df2.sort_index().index,
)
tm.assert_frame_equal(result, expected)
