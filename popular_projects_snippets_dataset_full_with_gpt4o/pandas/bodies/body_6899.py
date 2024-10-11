# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# https://github.com/pandas-dev/pandas/issues/24959
idx = Index([1, pd.Timestamp("2000")])
# default (sort=None)
with tm.assert_produces_warning(RuntimeWarning):
    result = idx.union(idx[:1])

tm.assert_index_equal(result, idx)

# sort=None
with tm.assert_produces_warning(RuntimeWarning):
    result = idx.union(idx[:1], sort=None)
tm.assert_index_equal(result, idx)

# sort=False
result = idx.union(idx[:1], sort=False)
tm.assert_index_equal(result, idx)
