# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked_shared.py
op = comparison_op

left = pd.array([0, 1, 2, None, None, None], dtype=dtype)
right = pd.array([0, 1, None, 0, 1, None], dtype=dtype)

result = op(left, right)
values = op(left._data, right._data)
mask = left._mask | right._mask

expected = pd.arrays.BooleanArray(values, mask)
tm.assert_extension_array_equal(result, expected)

# ensure we haven't mutated anything inplace
result[0] = pd.NA
tm.assert_extension_array_equal(
    left, pd.array([0, 1, 2, None, None, None], dtype=dtype)
)
tm.assert_extension_array_equal(
    right, pd.array([0, 1, None, 0, 1, None], dtype=dtype)
)
