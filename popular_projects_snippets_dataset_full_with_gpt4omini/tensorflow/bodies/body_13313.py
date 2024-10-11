# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Compute a n x n symmetric projection matrix.

    Args:
      n: Dimension.

    Returns:
      A n x n symmetric projection matrix, i.e. a matrix P s.t. P=P*P, P=P^T.
    """
q = self._orthogonal_matrix(n)
# randomly zeroing out some columns
mask = math_ops.cast(
    random_ops.random_normal([n], seed=self.seed) > 0, self.dtype)
if self.seed:
    self.seed += 1
c = math_ops.multiply(q, mask)
exit(math_ops.matmul(c, array_ops.matrix_transpose(c)))
