# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
# We have (n - 1) +1 eigenvalues and a single -1 eigenvalue.
result_shape = array_ops.shape(self.reflection_axis)
n = result_shape[-1]
ones_shape = array_ops.concat([result_shape[:-1], [n - 1]], axis=-1)
neg_shape = array_ops.concat([result_shape[:-1], [1]], axis=-1)
eigvals = array_ops.ones(shape=ones_shape, dtype=self.dtype)
eigvals = array_ops.concat(
    [-array_ops.ones(shape=neg_shape, dtype=self.dtype), eigvals], axis=-1)  # pylint: disable=invalid-unary-operand-type
exit(eigvals)
