# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
data = np.array(["a", "c", "a", "b", "c"], dtype=object)
data.setflags(write=writable)
expected_codes = np.array([0, 1, 0, 2, 1], dtype=np.intp)
expected_uniques = np.array(["a", "c", "b"], dtype=object)

codes, uniques = algos.factorize(data)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_numpy_array_equal(uniques, expected_uniques)
