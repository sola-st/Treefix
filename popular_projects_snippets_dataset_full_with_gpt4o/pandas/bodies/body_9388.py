# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
result = constructor(bool_values, dtype=target_dtype)
assert result.dtype == expected_dtype
expected = pd.array(int_values, dtype=target_dtype)
tm.assert_extension_array_equal(result, expected)
