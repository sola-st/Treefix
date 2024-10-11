# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py

# make sure that we are setting the axes
# correctly when on axis=0 or 1
# in the presence of a non-monotonic indexer
# GH12713

base = tsframe.iloc[0:5]
r = len(base.index)
c = len(base.columns)
tso = DataFrame(
    np.random.randn(r, c), index=base.index, columns=base.columns, dtype="float64"
)
# monotonic
ts = tso
grouped = ts.groupby(lambda x: x.weekday(), group_keys=False)
result = ts - grouped.transform("mean")
expected = grouped.apply(lambda x: x - x.mean(axis=0))
tm.assert_frame_equal(result, expected)

ts = ts.T
grouped = ts.groupby(lambda x: x.weekday(), axis=1, group_keys=False)
result = ts - grouped.transform("mean")
expected = grouped.apply(lambda x: (x.T - x.mean(1)).T)
tm.assert_frame_equal(result, expected)

# non-monotonic
ts = tso.iloc[[1, 0] + list(range(2, len(base)))]
grouped = ts.groupby(lambda x: x.weekday(), group_keys=False)
result = ts - grouped.transform("mean")
expected = grouped.apply(lambda x: x - x.mean(axis=0))
tm.assert_frame_equal(result, expected)

ts = ts.T
grouped = ts.groupby(lambda x: x.weekday(), axis=1, group_keys=False)
result = ts - grouped.transform("mean")
expected = grouped.apply(lambda x: (x.T - x.mean(1)).T)
tm.assert_frame_equal(result, expected)
