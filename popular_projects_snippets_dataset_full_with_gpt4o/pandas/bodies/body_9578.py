# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
result = pd.array(bool_values, dtype=target_dtype)
assert result.dtype == expected_dtype
expected = pd.array(values, dtype=target_dtype)
tm.assert_extension_array_equal(result, expected)
