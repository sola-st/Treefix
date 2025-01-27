# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
df = tm.makeTimeDataFrame()

grouped = df.groupby(lambda x: x.year)
grouper = grouped.grouper.groupings[0].grouping_vector
grouped.grouper.groupings[0] = Grouping(ts.index, list(grouper))

result = grouped.agg(np.mean)
expected = grouped.mean()
tm.assert_frame_equal(result, expected)

grouped.grouper.groupings[0] = Grouping(ts.index, tuple(grouper))

result = grouped.agg(np.mean)
expected = grouped.mean()
tm.assert_frame_equal(result, expected)
