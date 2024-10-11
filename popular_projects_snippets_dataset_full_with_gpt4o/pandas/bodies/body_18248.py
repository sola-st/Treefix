# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# numpy does not allow powers of negative integers so test separately
# https://github.com/numpy/numpy/pull/8127
idx1 = idx1._rename("foo")
idx2 = idx2._rename("bar")
result = pow(idx1, idx2)
expected = pow(Index(idx1.to_numpy()), Index(idx2.to_numpy()))
tm.assert_index_equal(result, expected, exact="equiv")
