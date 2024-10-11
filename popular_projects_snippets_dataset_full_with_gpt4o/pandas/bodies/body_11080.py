# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
mapping = {"A": 0, "B": 0, "C": 1, "D": 1}
grouped = tsframe.groupby(mapping, axis=1)

# aggregate
aggregated = grouped.aggregate(np.mean)
assert len(aggregated) == len(tsframe)
assert len(aggregated.columns) == 2

# transform
tf = lambda x: x - x.mean()
groupedT = tsframe.T.groupby(mapping, axis=0)
tm.assert_frame_equal(groupedT.transform(tf).T, grouped.transform(tf))

# iterate
for k, v in grouped:
    assert len(v.columns) == 2
