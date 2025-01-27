# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# https://github.com/pandas-dev/pandas/issues/24959
idx = MultiIndex.from_product([[1, 0], ["a", "b"]])

# default, sort=None
other = idx[slice_]
tm.assert_index_equal(idx.union(other), idx)
tm.assert_index_equal(other.union(idx), idx)

# sort=False
tm.assert_index_equal(idx.union(other, sort=False), idx)
