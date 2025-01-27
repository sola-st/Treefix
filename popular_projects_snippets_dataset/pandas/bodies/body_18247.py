# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
result = op(idx, scalar)
expected = op(Index(idx.to_numpy()), scalar)
tm.assert_index_equal(result, expected, exact="equiv")
