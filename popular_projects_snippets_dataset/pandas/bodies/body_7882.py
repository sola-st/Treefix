# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_factorize.py
# GH 17927
array = [1, 2, 2 + 1j]
labels, uniques = factorize(array)

expected_labels = np.array([0, 1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(labels, expected_labels)

# Should return a complex dtype in the future
expected_uniques = np.array([(1 + 0j), (2 + 0j), (2 + 1j)], dtype=object)
tm.assert_numpy_array_equal(uniques, expected_uniques)
