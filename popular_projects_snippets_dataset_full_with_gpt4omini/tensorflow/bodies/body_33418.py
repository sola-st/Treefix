# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = linalg_lib.LinearOperatorFullMatrix(
    [[1., 2.], [2., 1.]], is_self_adjoint=True)
self.assertTrue(linear_operator_util.is_adjoint_pair(x, x))
