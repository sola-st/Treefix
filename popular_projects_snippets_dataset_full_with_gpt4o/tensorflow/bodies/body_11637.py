# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Get dense shape and dtype of the tf.Tensor containing the matrix.

  Args:
    matrix: A `tf.Tensor` of type `tf.variant` storing a sparse matrix.

  Returns:
    An instance of `ShapeAndType` with properties `shape` (a `tf.TensorShape`)
    and `dtype` (a `tf.DType`).

  Raises:
    TypeError: if `matrix` is not a tensor or its dtype is not variant.
    ValueError: if `matrix` lacks static handle data containing the dense
      shape and dtype.
  """
if not isinstance(matrix, ops.Tensor):
    raise TypeError("matrix should be a tensor, but saw: %s" % (matrix,))
if matrix.dtype != dtypes.variant:
    raise TypeError(
        "expected matrix to be type tf.variant, but saw: %s" % (matrix.dtype,))
handle_data = _get_handle_data(matrix)
if not handle_data or not handle_data.is_set:
    raise ValueError("matrix has missing handle data: %s" % (matrix,))
if len(handle_data.shape_and_type) != 1:
    raise ValueError("len(matrix.handle_data.shape_and_type) != 1: '%s'" %
                     (handle_data.shape_and_type,))
exit(DenseShapeAndType(
    tensor_shape.TensorShape(handle_data.shape_and_type[0].shape),
    dtypes.DType(handle_data.shape_and_type[0].dtype)))
