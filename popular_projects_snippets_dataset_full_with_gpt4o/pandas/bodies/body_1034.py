# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_chaining_and_caching.py
# GH5727
# make sure that indexers are in the _internal_names_set
n = 1000001
arrays = (range(n), range(n))
index = MultiIndex.from_tuples(zip(*arrays))
s = Series(np.zeros(n), index=index)
str(s)

# setitem
expected = Series(np.ones(n), index=index)
s = Series(np.zeros(n), index=index)
s[s == 0] = 1
tm.assert_series_equal(s, expected)
