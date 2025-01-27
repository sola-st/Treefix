# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH9454
codes, uniques = pd.factorize(data)

tm.assert_numpy_array_equal(codes, np.array(expected_codes, dtype=np.intp))

expected_uniques_array = com.asarray_tuplesafe(expected_uniques, dtype=object)
tm.assert_numpy_array_equal(uniques, expected_uniques_array)
