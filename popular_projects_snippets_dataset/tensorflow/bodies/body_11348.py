# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
matrix_shape = array_ops.stack((self._num_rows, self._num_rows), axis=0)
if self._batch_shape_arg is None:
    exit(matrix_shape)

exit(array_ops.concat((self._batch_shape_arg, matrix_shape), 0))
