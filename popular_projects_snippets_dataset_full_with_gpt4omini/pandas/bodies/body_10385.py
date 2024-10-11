# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
grouped = ts.groupby(lambda x: x.month)
result = grouped.transform(np.mean)

tm.assert_index_equal(result.index, ts.index)
for _, gp in grouped:
    assert_fp_equal(result.reindex(gp.index), gp.mean())

grouped = tsframe.groupby(lambda x: x.month)
result = grouped.transform(np.mean)
tm.assert_index_equal(result.index, tsframe.index)
for _, gp in grouped:
    agged = gp.mean(axis=0)
    res = result.reindex(gp.index)
    for col in tsframe:
        assert_fp_equal(res[col], agged[col])

    # group columns
grouped = tsframe.groupby({"A": 0, "B": 0, "C": 1, "D": 1}, axis=1)
result = grouped.transform(np.mean)
tm.assert_index_equal(result.index, tsframe.index)
tm.assert_index_equal(result.columns, tsframe.columns)
for _, gp in grouped:
    agged = gp.mean(1)
    res = result.reindex(columns=gp.columns)
    for idx in gp.index:
        assert_fp_equal(res.xs(idx), agged[idx])
