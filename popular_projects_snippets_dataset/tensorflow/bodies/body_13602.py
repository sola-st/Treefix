# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
x = self._variance_scale_term() * self._mean()
# pylint: disable=invalid-unary-operand-type
exit(array_ops.matrix_set_diag(
    -math_ops.matmul(
        x[..., array_ops.newaxis],
        x[..., array_ops.newaxis, :]),  # outer prod
    self._variance()))
