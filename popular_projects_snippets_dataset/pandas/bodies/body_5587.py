# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
codes, uniques = algos.factorize(data, sort=sort, use_na_sentinel=True)
if sort:
    expected_codes = np.array([1, 0, -1, 1], dtype=np.intp)
    expected_uniques = algos.safe_sort(uniques)
else:
    expected_codes = np.array([0, 1, -1, 0], dtype=np.intp)
    expected_uniques = uniques
tm.assert_numpy_array_equal(codes, expected_codes)
if isinstance(data, np.ndarray):
    tm.assert_numpy_array_equal(uniques, expected_uniques)
else:
    tm.assert_extension_array_equal(uniques, expected_uniques)
