# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
x = Series(
    data=[1, 2, 3], index=MultiIndex.from_tuples([("A", 1), ("A", 2), ("B", 3)])
)

y = Series(
    data=[4, 5, 6], index=MultiIndex.from_tuples([("Z", 1), ("Z", 2), ("B", 3)])
)

res = x - y
exp_index = x.index.union(y.index)
exp = x.reindex(exp_index) - y.reindex(exp_index)
tm.assert_series_equal(res, exp)

# hit non-monotonic code path
res = x[::-1] - y[::-1]
exp_index = x.index.union(y.index)
exp = x.reindex(exp_index) - y.reindex(exp_index)
tm.assert_series_equal(res, exp)
