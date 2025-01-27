# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH#49549
data = np.array([1, 2, 3, 1, np.nan])
rizer = ht.ObjectFactorizer(len(data))
result = rizer.factorize(data.astype(object))
expected = np.array([0, 1, 2, 0, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
expected_uniques = np.array([1, 2, 3], dtype=object)
tm.assert_numpy_array_equal(rizer.uniques.to_array(), expected_uniques)
