# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# numpy does not allow powers of negative integers so test separately
# https://github.com/numpy/numpy/pull/8127
result = pow(idx, scalar)
expected = pow(Index(idx.to_numpy()), scalar)
tm.assert_index_equal(result, expected, exact="equiv")
