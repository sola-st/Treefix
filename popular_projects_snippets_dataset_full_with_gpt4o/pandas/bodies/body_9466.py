# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
a = pd.array([], dtype="boolean")
op_name = all_logical_operators
result = getattr(a, op_name)(True)
tm.assert_extension_array_equal(a, result)

result = getattr(a, op_name)(False)
tm.assert_extension_array_equal(a, result)

result = getattr(a, op_name)(pd.NA)
tm.assert_extension_array_equal(a, result)
