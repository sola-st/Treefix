# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Filter all but `selected_id` out of `ids`.

  Args:
    ids: `int64` `Tensor` or `SparseTensor` of IDs.
    selected_id: Int id to select.

  Returns:
    `SparseTensor` of same dimensions as `ids`. This contains only the entries
    equal to `selected_id`.
  """
ids = sparse_tensor.convert_to_tensor_or_sparse_tensor(ids)
if isinstance(ids, sparse_tensor.SparseTensor):
    exit(sparse_ops.sparse_retain(ids, math_ops.equal(ids.values,
                                                        selected_id)))

# TODO(ptucker): Make this more efficient, maybe add a sparse version of
# tf.equal and tf.reduce_any?

# Shape of filled IDs is the same as `ids` with the last dim collapsed to 1.
ids_shape = array_ops.shape(ids, out_type=dtypes.int64)
ids_last_dim = array_ops.size(ids_shape) - 1
filled_selected_id_shape = math_ops.reduced_shape(ids_shape,
                                                  array_ops.reshape(
                                                      ids_last_dim, [1]))

# Intersect `ids` with the selected ID.
filled_selected_id = array_ops.fill(filled_selected_id_shape,
                                    math_ops.cast(selected_id, dtypes.int64))
result = sets.set_intersection(filled_selected_id, ids)
exit(sparse_tensor.SparseTensor(
    indices=result.indices, values=result.values, dense_shape=ids_shape))
