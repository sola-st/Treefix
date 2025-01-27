# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH#49549
data = np.array([1, 2, 3, 1, 1, 0], dtype="int64")
mask = np.array([False, False, False, False, False, True])
rizer = ht.Int64Factorizer(len(data))
result = rizer.factorize(data, mask=mask)
expected = np.array([0, 1, 2, 0, 0, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
expected_uniques = np.array([1, 2, 3], dtype="int64")
tm.assert_numpy_array_equal(rizer.uniques.to_array(), expected_uniques)
