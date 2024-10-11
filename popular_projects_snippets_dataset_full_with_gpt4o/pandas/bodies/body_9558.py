# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_comparison.py
op = comparison_op
a = pd.array([0, 1, None] * 3, dtype="Int64")
b = pd.array([0] * 3 + [1] * 3 + [None] * 3, dtype="Float64")
other = b.astype("Int64")
expected = op(a, other)
result = op(a, b)
tm.assert_extension_array_equal(result, expected)
expected = op(other, a)
result = op(b, a)
tm.assert_extension_array_equal(result, expected)
