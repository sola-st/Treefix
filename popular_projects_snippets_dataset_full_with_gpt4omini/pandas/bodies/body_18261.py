# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_array_ops.py
left = np.arange(9).reshape(3, 3).astype(object)
right = left.T

result = comparison_op(left, right, operator.eq)
expected = np.eye(3).astype(bool)
tm.assert_numpy_array_equal(result, expected)

# Ensure that cython doesn't raise on non-writeable arg, which
#  we can get from np.broadcast_to
right.flags.writeable = False
result = comparison_op(left, right, operator.ne)
tm.assert_numpy_array_equal(result, ~expected)
