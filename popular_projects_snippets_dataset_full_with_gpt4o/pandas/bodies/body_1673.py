# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
values = np.array(["b", nulls_fixture, "a", "b"], dtype=object)
result = safe_sort(values)
expected = np.array(["a", "b", "b", nulls_fixture], dtype=object)
tm.assert_numpy_array_equal(result, expected)
