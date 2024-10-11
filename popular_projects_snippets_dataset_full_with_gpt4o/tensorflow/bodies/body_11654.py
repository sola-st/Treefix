# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Construct a CSRSparseMatrix from a dense matrix or SparseTensor.

    Args:
      value: A dense `2D` or `3D` Tensor or `SparseTensor`.
      indices: The nonzero indices of `value`
        (if `value` is not a `SparseTensor`).
      name: Optional op name.

    Raises:
      ValueError: if `value` is a `SparseTensor` and `indices` is not `None`.
    """
del name  # Unused.
super(CSRSparseMatrix, self).__init__()
if isinstance(value, sparse_tensor.SparseTensor):
    if indices is not None:
        raise ValueError("indices must be None if value is a SparseTensor.")
    self._dtype = value.dtype
    self._csr_matrix = sm_ops.sparse_tensor_to_csr_sparse_matrix(
        indices=value.indices,
        values=value.values,
        dense_shape=value.dense_shape)
else:
    value = ops.convert_to_tensor(value)
    self._dtype = value.dtype
    if indices is not None:
        indices = ops.convert_to_tensor(indices, dtype=dtypes.int64)
    else:
        indices = array_ops.stop_gradient(array_ops.where(value))
    self._csr_matrix = sm_ops.dense_to_csr_sparse_matrix(value, indices)

# Eager mode doesn't call shape inference functions, so we have to set the
# shape and dtype handle data directly.
if self._eager_mode:
    # pylint: disable=protected-access
    self._csr_matrix._handle_data = _make_handle_data(value)
    # pylint: enable=protected-access
