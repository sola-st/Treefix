# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_array_ops.py
left = np.arange(8).reshape(4, 2)
right = left.astype(object)
right[0, 0] = np.nan

# Check that we fall back to the vec_binop branch
with pytest.raises(TypeError, match="unsupported operand type"):
    operator.or_(left, right)

result = na_logical_op(left, right, operator.or_)
expected = right
tm.assert_numpy_array_equal(result, expected)
