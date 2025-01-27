# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx1 = idx1._rename("foo")
idx2 = idx2._rename("bar")
result = op(idx1, idx2)
expected = op(Index(idx1.to_numpy()), Index(idx2.to_numpy()))
tm.assert_index_equal(result, expected, exact="equiv")
