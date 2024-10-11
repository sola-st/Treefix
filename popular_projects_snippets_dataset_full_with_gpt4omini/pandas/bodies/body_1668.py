# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
values = np.array(["b", 1, 0, "a"], dtype=object)
codes = [0, 1, 2, 3, 0, -1, 1]
result, result_codes = safe_sort(values, codes)
expected = np.array([0, 1, "a", "b"], dtype=object)
expected_codes = np.array([3, 1, 0, 2, 3, -1, 1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
tm.assert_numpy_array_equal(result_codes, expected_codes)
