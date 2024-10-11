# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_lower_triangular_test.py
operator1 = linalg_lib.LinearOperatorLowerTriangular(
    [[1., 0., 0.], [2., 1., 0.], [2., 3., 3.]])
operator2 = linalg_lib.LinearOperatorDiag([2., 2., 3.])
operator_matmul = operator1.matmul(operator2)
self.assertTrue(isinstance(
    operator_matmul,
    linalg_lib.LinearOperatorLowerTriangular))
self.assertAllClose(
    math_ops.matmul(
        operator1.to_dense(),
        operator2.to_dense()),
    self.evaluate(operator_matmul.to_dense()))

operator_matmul = operator2.matmul(operator1)
self.assertTrue(isinstance(
    operator_matmul,
    linalg_lib.LinearOperatorLowerTriangular))
self.assertAllClose(
    math_ops.matmul(
        operator2.to_dense(),
        operator1.to_dense()),
    self.evaluate(operator_matmul.to_dense()))
