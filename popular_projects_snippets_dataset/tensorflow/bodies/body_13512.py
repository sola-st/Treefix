# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/multinomial.py
p = self.probs * array_ops.ones_like(
    self.total_count)[..., array_ops.newaxis]
# pylint: disable=invalid-unary-operand-type
exit(array_ops.matrix_set_diag(
    -math_ops.matmul(
        self._mean_val[..., array_ops.newaxis],
        p[..., array_ops.newaxis, :]),  # outer product
    self._variance()))
