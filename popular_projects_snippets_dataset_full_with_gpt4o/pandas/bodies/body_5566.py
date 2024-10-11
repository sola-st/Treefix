# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH#35667
values = np.array([1, 2, 1, np.nan])
ser = Series(values)
codes, uniques = ser.factorize(use_na_sentinel=False)

expected_codes = np.array([0, 1, 0, 2], dtype=np.intp)
expected_uniques = Index([1.0, 2.0, np.nan])

tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_index_equal(uniques, expected_uniques)
