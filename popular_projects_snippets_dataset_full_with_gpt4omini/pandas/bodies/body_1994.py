# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
transform, assert_equal = transform_assert_equal
result = to_numeric(transform(data))

expected = transform(exp)
assert_equal(result, expected)
