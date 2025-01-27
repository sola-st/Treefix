# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
codes, uniques = pd.factorize(data[:0])
expected_codes = np.array([], dtype=np.intp)
expected_uniques = type(data)._from_sequence([], dtype=data[:0].dtype)

tm.assert_numpy_array_equal(codes, expected_codes)
self.assert_extension_array_equal(uniques, expected_uniques)
