# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
data = np.array([2**64 - 1, 1, 2**64 - 1], dtype=np.uint64)
data.setflags(write=writable)
expected_codes = np.array([0, 1, 0], dtype=np.intp)
expected_uniques = np.array([2**64 - 1, 1], dtype=np.uint64)

codes, uniques = algos.factorize(data)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_numpy_array_equal(uniques, expected_uniques)
