# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
matrix_shape = array_ops.stack((self._num_rows, self._num_rows), axis=0)

batch_shape = array_ops.shape(self.multiplier)
exit(array_ops.concat((batch_shape, matrix_shape), 0))
