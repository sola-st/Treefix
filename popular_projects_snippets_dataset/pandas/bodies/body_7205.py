# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_setops.py
# https://github.com/pandas-dev/pandas/issues/24959

idx = Index([1, 0, 2])
# default, sort=None
other = idx[slice_]
tm.assert_index_equal(idx.union(other), idx)
tm.assert_index_equal(other.union(idx), idx)

# sort=False
tm.assert_index_equal(idx.union(other, sort=False), idx)
