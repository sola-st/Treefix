# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
values = [3, 1, 2, 0, 4]
expected = np.array([0, 1, 2, 3, 4])

result, result_codes = safe_sort(
    values, codes, use_na_sentinel=True, verify=verify
)
expected_codes = np.array(exp_codes, dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
tm.assert_numpy_array_equal(result_codes, expected_codes)
