# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
codes, uniques = algos.factorize(data, use_na_sentinel=False)

tm.assert_numpy_array_equal(uniques, expected_uniques, strict_nan=True)
tm.assert_numpy_array_equal(codes, expected_codes, strict_nan=True)
