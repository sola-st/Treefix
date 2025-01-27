# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_permutation.py
# Permutation matrices have determinant +/- 1.
exit(array_ops.zeros(shape=self.batch_shape_tensor(), dtype=self.dtype))
