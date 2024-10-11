# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_util.py
# product of empty factors
expected1 = np.array([], dtype=np.asarray(x).dtype)
expected2 = np.array([], dtype=np.asarray(y).dtype)
result1, result2 = cartesian_product([x, y])
tm.assert_numpy_array_equal(result1, expected1)
tm.assert_numpy_array_equal(result2, expected2)
