# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
result = safe_sort(arg)
expected = np.array(exp)
tm.assert_numpy_array_equal(result, expected)
