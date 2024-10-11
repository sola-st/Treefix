# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH9344, GH9049
idx_names = ["x", "y"]
idx = MultiIndex.from_tuples([(1, 1), (1, 2), (3, 4), (5, 6)], names=idx_names)
df = DataFrame(np.arange(12).reshape(-1, 3), index=idx)

by_levels = df.groupby(level=idx_names).mean()
# reset_index changes columns dtype to object
by_columns = df.reset_index().groupby(idx_names).mean()

# without casting, by_columns.columns is object-dtype
by_columns.columns = by_columns.columns.astype(np.int64)
tm.assert_frame_equal(by_levels, by_columns)
