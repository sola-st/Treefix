# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
y = constant_op.constant([3., 4.])
# Make a [2, N, N] shaped operator.
x = x * y[..., array_ops.newaxis, array_ops.newaxis]
operator = linalg.LinearOperatorFullMatrix(
    x, is_square=True)
exit(operator)
