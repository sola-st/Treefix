# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = linalg_lib.LinearOperatorFullMatrix(
    [[1., 2.], [3., 4.]], is_self_adjoint=False)
y = linalg_lib.LinearOperatorFullMatrix(
    [[10., 20.], [3., 4.]], is_self_adjoint=False)
self.assertFalse(linear_operator_util.is_adjoint_pair(x, y))
