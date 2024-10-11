# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
idx = Index([1, 2, 3], dtype=object)
result = idx.intersection(idx[1:])
expected = idx[1:]
tm.assert_index_equal(result, expected)

# if other is not monotonic increasing, intersection goes through
#  a different route
result = idx.intersection(idx[1:][::-1])
tm.assert_index_equal(result, expected)

result = idx._union(idx[1:], sort=None)
expected = idx
tm.assert_numpy_array_equal(result, expected.values)

result = idx.union(idx[1:], sort=None)
tm.assert_index_equal(result, expected)

# if other is not monotonic increasing, _union goes through
#  a different route
result = idx._union(idx[1:][::-1], sort=None)
tm.assert_numpy_array_equal(result, expected.values)

result = idx.union(idx[1:][::-1], sort=None)
tm.assert_index_equal(result, expected)
