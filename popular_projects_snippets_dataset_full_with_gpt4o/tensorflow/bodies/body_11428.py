# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
# Orthogonal matrix -> log|Q| = 0.
exit(array_ops.zeros(shape=self.batch_shape_tensor(), dtype=self.dtype))
