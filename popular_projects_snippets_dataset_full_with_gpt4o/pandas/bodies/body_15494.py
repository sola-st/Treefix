# Extracted from ./data/repos/pandas/pandas/tests/series/test_subclass.py
s = tm.SubclassedSeries([1, 2, 3, 4], index=list("abcd"))
res = getattr(s, idx_method)[indexer]
exp = tm.SubclassedSeries(exp_data, index=list(exp_idx))
tm.assert_series_equal(res, exp)
