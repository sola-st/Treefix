# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked_shared.py
op = comparison_op
left = pd.array([1, 0, None], dtype=dtype)

result = op(left, other)

if other is pd.NA:
    expected = pd.array([None, None, None], dtype="boolean")
else:
    values = op(left._data, other)
    expected = pd.arrays.BooleanArray(values, left._mask, copy=True)
tm.assert_extension_array_equal(result, expected)

# ensure we haven't mutated anything inplace
result[0] = pd.NA
tm.assert_extension_array_equal(left, pd.array([1, 0, None], dtype=dtype))
