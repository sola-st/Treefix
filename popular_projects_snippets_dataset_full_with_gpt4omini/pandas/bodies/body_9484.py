# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_comparison.py
op = comparison_op
a = pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype="boolean")
b = pd.array([True, False, None] * 3, dtype="boolean")

result = op(a, b)

values = op(a._data, b._data)
mask = a._mask | b._mask
expected = BooleanArray(values, mask)
tm.assert_extension_array_equal(result, expected)

# ensure we haven't mutated anything inplace
result[0] = None
tm.assert_extension_array_equal(
    a, pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype="boolean")
)
tm.assert_extension_array_equal(
    b, pd.array([True, False, None] * 3, dtype="boolean")
)
