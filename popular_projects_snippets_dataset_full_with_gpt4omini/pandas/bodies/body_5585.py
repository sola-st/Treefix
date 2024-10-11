# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# arrays that include the NA default for that type, but isn't used.
codes, uniques = algos.factorize(data)
expected_uniques = data[[0, 1]]
expected_codes = np.array([0, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_numpy_array_equal(uniques, expected_uniques)
