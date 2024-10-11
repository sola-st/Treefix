# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sets_impl.py
"""Compute set operation of elements in last dimension of `a` and `b`.

  All but the last dimension of `a` and `b` must match.

  Args:
    a: `Tensor` or `SparseTensor` of the same type as `b`. If sparse, indices
      must be sorted in row-major order.
    b: `Tensor` or `SparseTensor` of the same type as `a`. Must be
      `SparseTensor` if `a` is `SparseTensor`. If sparse, indices must be sorted
      in row-major order.
    set_operation: String indicating set operation. See
        SetOperationOp::SetOperationFromContext for valid values.
    validate_indices: Whether to validate the order and range of sparse indices
      in `a` and `b`.

  Returns:
    A `SparseTensor` with the same rank as `a` and `b`, and all but the last
    dimension the same. Elements along the last dimension contain the results
    of the set operation.

  Raises:
    TypeError: If inputs are invalid types.
    ValueError: If `a` is sparse and `b` is dense.
  """
if isinstance(a, sparse_tensor.SparseTensor):
    if isinstance(b, sparse_tensor.SparseTensor):
        indices, values, shape = gen_set_ops.sparse_to_sparse_set_operation(
            a.indices, a.values, a.dense_shape, b.indices, b.values,
            b.dense_shape, set_operation, validate_indices)
    else:
        raise ValueError("Sparse,Dense is not supported, but Dense,Sparse is. "
                         "Please flip the order of your inputs.")
elif isinstance(b, sparse_tensor.SparseTensor):
    indices, values, shape = gen_set_ops.dense_to_sparse_set_operation(
        a, b.indices, b.values, b.dense_shape, set_operation, validate_indices)
else:
    indices, values, shape = gen_set_ops.dense_to_dense_set_operation(
        a, b, set_operation, validate_indices)
exit(sparse_tensor.SparseTensor(indices, values, shape))
