# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
matrix_shape = tensor_shape.TensorShape((self._num_rows_static,
                                         self._num_rows_static))

batch_shape = self.multiplier.shape
exit(batch_shape.concatenate(matrix_shape))
