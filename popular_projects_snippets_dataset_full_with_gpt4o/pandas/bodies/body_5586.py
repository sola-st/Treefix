# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
codes, uniques = algos.factorize_array(data, na_value=na_value)
expected_uniques = data[[1, 3]]
expected_codes = np.array([-1, 0, -1, 1], dtype=np.intp)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_numpy_array_equal(uniques, expected_uniques)
