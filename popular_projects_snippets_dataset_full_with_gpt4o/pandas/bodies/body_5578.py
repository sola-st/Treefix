# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
data = np.array([2**63 - 1, -(2**63), 2**63 - 1], dtype=np.int64)
data.setflags(write=writable)
expected_codes = np.array([0, 1, 0], dtype=np.intp)
expected_uniques = np.array([2**63 - 1, -(2**63)], dtype=np.int64)

codes, uniques = algos.factorize(data)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_numpy_array_equal(uniques, expected_uniques)
