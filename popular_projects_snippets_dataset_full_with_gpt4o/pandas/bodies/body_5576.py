# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
data = np.array([1.0, 1e8, 1.0, 1e-8, 1e8, 1.0], dtype=np.float64)
data.setflags(write=writable)
expected_codes = np.array([0, 1, 0, 2, 1, 0], dtype=np.intp)
expected_uniques = np.array([1.0, 1e8, 1e-8], dtype=np.float64)

codes, uniques = algos.factorize(data)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_numpy_array_equal(uniques, expected_uniques)
