# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
result = np.array([Series(input_dict)])
tm.assert_numpy_array_equal(result, expected)
