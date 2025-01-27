# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# go through _aggregate_frame with self.axis == 0 and duplicate columns
tsframe.columns = ["A", "B", "A", "C"]
gb = tsframe.groupby(lambda x: x.month, as_index=as_index)

res = gb.agg(np.percentile, 80, axis=0)

ex_data = {
    1: tsframe[tsframe.index.month == 1].quantile(0.8),
    2: tsframe[tsframe.index.month == 2].quantile(0.8),
}
expected = DataFrame(ex_data).T
expected.index = expected.index.astype(np.int32)
if not as_index:
    # TODO: try to get this more consistent?
    expected.index = Index(range(2))

tm.assert_frame_equal(res, expected)
