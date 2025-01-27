# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# Check that we return all -1s and do not raise or cast incorrectly

dti = date_range("2016-01-01", periods=3)
pi = dti.to_period("D")
pi2 = dti.to_period("W")

expected = np.array([-1, -1, -1], dtype=np.intp)

result = pi.get_indexer(dti)
tm.assert_numpy_array_equal(result, expected)

# This should work in both directions
result = dti.get_indexer(pi)
tm.assert_numpy_array_equal(result, expected)

result = pi.get_indexer(pi2)
tm.assert_numpy_array_equal(result, expected)

# We expect the same from get_indexer_non_unique
result = pi.get_indexer_non_unique(dti)[0]
tm.assert_numpy_array_equal(result, expected)

result = dti.get_indexer_non_unique(pi)[0]
tm.assert_numpy_array_equal(result, expected)

result = pi.get_indexer_non_unique(pi2)[0]
tm.assert_numpy_array_equal(result, expected)
