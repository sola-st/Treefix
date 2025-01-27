# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
grouped = mframe.groupby(["A", "B"])

result = grouped.agg(np.mean)
expected = grouped.mean()
tm.assert_frame_equal(result, expected)
