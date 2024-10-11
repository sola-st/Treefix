# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
values = [3, 1, 2, 0, 4]
expected = np.array([0, 1, 2, 3, 4])

# out of bound indices
codes = [0, 101, 102, 2, 3, 0, 99, 4]
result, result_codes = safe_sort(values, codes, use_na_sentinel=True)
expected_codes = np.array([3, -1, -1, 2, 0, 3, -1, 4], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
tm.assert_numpy_array_equal(result_codes, expected_codes)
