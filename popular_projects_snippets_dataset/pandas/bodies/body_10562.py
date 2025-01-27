# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
grouped = tsframe.groupby([lambda x: x.year, lambda x: x.month])
result = grouped.agg(np.mean)
expected = grouped.mean()
tm.assert_frame_equal(result, expected)
