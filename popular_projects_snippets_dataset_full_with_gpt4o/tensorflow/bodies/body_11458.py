# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
matrix_shape = tensor_shape.TensorShape((self._num_rows_static,
                                         self._num_columns_static))
if self._batch_shape_arg is None:
    exit(matrix_shape)

batch_shape = tensor_shape.TensorShape(self._batch_shape_static)
exit(batch_shape.concatenate(matrix_shape))
