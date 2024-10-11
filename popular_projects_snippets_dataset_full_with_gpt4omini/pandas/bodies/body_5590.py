# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 19721
codes, uniques = algos.factorize(data)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_index_equal(uniques, expected_uniques)
