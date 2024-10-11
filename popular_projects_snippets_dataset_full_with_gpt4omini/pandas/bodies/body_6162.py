# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
codes, uniques = pd.factorize(data_for_grouping, use_na_sentinel=True)
expected_codes = np.array([0, 0, -1, -1, 1, 1, 0, 2], dtype=np.intp)
expected_uniques = data_for_grouping.take([0, 4, 7])

tm.assert_numpy_array_equal(codes, expected_codes)
self.assert_extension_array_equal(uniques, expected_uniques)
