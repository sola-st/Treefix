# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
# override because we only have 2 unique values
labels, uniques = pd.factorize(data_for_grouping, use_na_sentinel=True)
expected_labels = np.array([0, 0, -1, -1, 1, 1, 0], dtype=np.intp)
expected_uniques = data_for_grouping.take([0, 4])

tm.assert_numpy_array_equal(labels, expected_labels)
self.assert_extension_array_equal(uniques, expected_uniques)
