# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
operator = linalg.LinearOperatorFullMatrix(
    [[1., 0.5], [0.5, 1.]],
    is_square=True,
    is_self_adjoint=True,
    is_non_singular=True,
    is_positive_definite=True)
methods = {
    "trace": linalg.trace,
    "diag_part": linalg.diag_part,
    "log_abs_determinant": linalg.logdet,
    "determinant": linalg.det
}
for method in methods:
    op_val = getattr(operator, method)()
    linalg_val = methods[method](operator)
    self.assertAllClose(
        self.evaluate(op_val),
        self.evaluate(linalg_val))
# Solve and Matmul go here.

adjoint = linalg.adjoint(operator)
self.assertIsInstance(adjoint, linalg.LinearOperator)
cholesky = linalg.cholesky(operator)
self.assertIsInstance(cholesky, linalg.LinearOperator)
inverse = linalg.inv(operator)
self.assertIsInstance(inverse, linalg.LinearOperator)
