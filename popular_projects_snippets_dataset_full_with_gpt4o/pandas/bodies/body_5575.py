# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH41132
dtype = any_real_numpy_dtype
data = np.array([1, 2, 2, 1], dtype=dtype)
expected_codes = np.array([0, 1, 1, 0], dtype=np.intp)
expected_uniques = np.array([1, 2], dtype=dtype)

codes, uniques = algos.factorize(data)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_numpy_array_equal(uniques, expected_uniques)
