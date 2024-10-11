# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# nothing to group, all NA
grouped = ts.groupby(ts * np.nan, group_keys=False)
assert ts.dtype == np.float64

# groupby float64 values results in a float64 Index
exp = Series([], dtype=np.float64, index=Index([], dtype=np.float64))
tm.assert_series_equal(grouped.sum(), exp)
tm.assert_series_equal(grouped.agg(np.sum), exp)
tm.assert_series_equal(grouped.apply(np.sum), exp, check_index_type=False)

# DataFrame
grouped = tsframe.groupby(tsframe["A"] * np.nan, group_keys=False)
exp_df = DataFrame(
    columns=tsframe.columns,
    dtype=float,
    index=Index([], name="A", dtype=np.float64),
)
tm.assert_frame_equal(grouped.sum(), exp_df)
tm.assert_frame_equal(grouped.agg(np.sum), exp_df)
tm.assert_frame_equal(grouped.apply(np.sum), exp_df)
