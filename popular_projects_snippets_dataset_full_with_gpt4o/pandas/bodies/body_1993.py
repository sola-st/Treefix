# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
transform, assert_equal = transform_assert_equal
data = transform(data)

result = to_numeric(data)
assert_equal(result, data)
