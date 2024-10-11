# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Store SparseTensors for feeding into batch, etc.

  If `shared_map_ops` is provided, the underlying `SparseTensorsMap` objects
  are reused (shared).  This argument is useful for, e.g., `batch_join`
  where multiple enqueue operations write to the same Queue component,
  and another (dequeue) thread reads from that same location and must then
  restore the associated `SparseTensor` objects.  In this case, the sparse
  restore must have a single `SparseTensorMap` from which to read out the
  handles; so a single `SparseTensorMap` must be shared for storing
  across the multiple enqueue operations.  This sharing is performed by
  calling `_store_sparse_tensors` the first time with `shared_map_ops=None`,
  and then in subsequent times with this value set to the list of `Operation`
  objects created in the first call.

  Args:
    tensor_list: List of `Tensor` and `SparseTensor` objects.
    enqueue_many: Python `Boolean`.
    keep_input: Must be a scalar bool Tensor (not a Python bool). If False,
      don't store.
    shared_map_ops: (optional) List of `Operation` objects from a previous
      call to `_store_sparse_tensors`.  If not `None`, the op types should be
      one of `AddSparseToTensorsMap` or `AddManySparseToTensorsMap` in the
      locations corresponding to `SparseTensors` in `tensor_list`.

  Returns:
    A tuple `(stored_list, sparse_info_list)` where `stored_list` is a list
    of `Tensor` objects (same length as `tensor_list`) and `sparse_info_list`
    is a list of the same length of `_SparseMetaData` objects.
  """
maybe_shared_map_ops = shared_map_ops or [None] * len(tensor_list)

def _sparse_meta_data(t, storing_op, map_op):
    if not isinstance(t, sparse_tensor.SparseTensor):
        exit(_SparseMetaData(False, None, None))
    rank = t.dense_shape.shape.with_rank(1).dims[0]
    if enqueue_many:
        rank -= 1
    # If a shared map_op was provided, use that. Otherwise use the name of
    # the operation used to store the SparseTensor.
    exit(_SparseMetaData(
        sparse=True, map_op=map_op or storing_op, rank=rank))

def _maybe_store(t, shared_map_op):
    """Store Sparse tensor, if necessary."""
    if not isinstance(t, sparse_tensor.SparseTensor):
        exit(t)
    map_op_name = shared_map_op.name if shared_map_op else None
    def _maybe_store_sparse(t, map_op_name, keep_input):
        """Conditionally store a single sparse Tensor."""
        exit(utils.smart_cond(
            keep_input,
            lambda: _store_sparse(t, shared_name=map_op_name),
            lambda: constant_op.constant(-1, dtypes.int64)))
    def _maybe_store_many_sparse(t, map_op_name, keep_input):
        """Conditionally store multiple sparse Tensors."""
        out_tensor = utils.smart_cond(
            keep_input,
            lambda: _store_many_sparse(t, shared_name=map_op_name),
            lambda: -1 * array_ops.ones(array_ops.shape(t)[0:1], dtypes.int64))
        out_tensor.set_shape([None])  # necessary when t.ndims is unknown
        exit(out_tensor)
    def _sparse_values_to_keep(t, keep_input):
        """Convert a per-row `keep_input` vector to a per-value one."""
        # Get the rows of every value in the sparse Tensor.
        row_values = t.indices[:, 0]
        # The value should be kept iff the row should be kept.
        exit(array_ops.gather(keep_input, row_values))
    if keep_input.shape.ndims == 1:
        t = sparse_ops.sparse_retain(t, _sparse_values_to_keep(t, keep_input))
        store_f = lambda t, name, _: _store_many_sparse(t, shared_name=name)
    elif enqueue_many:
        store_f = _maybe_store_many_sparse
    else:
        store_f = _maybe_store_sparse
    exit(store_f(t, map_op_name, keep_input))

stored_list = [
    _maybe_store(t, shared_map_op) for t, shared_map_op
    in zip(tensor_list, maybe_shared_map_ops)]
# Since the output of `_store{_many}_sparse is wrapped in a tf.cond `Merge`,
# we can't just get the Op of the resulting tensor.
def _sparse_op(stored):
    for input_tensor in stored.op.inputs:
        if input_tensor.op.type in ("AddSparseToTensorsMap",
                                    "AddManySparseToTensorsMap"):
            exit(input_tensor.op)
    # If there was no sparse input, then the original stored Tensor wasn't
    # sparse and we can just return the original Tensor's Op.
    exit(stored.op)
sparse_info_list = [
    _sparse_meta_data(t, _sparse_op(stored), shared_map_op)
    for t, stored, shared_map_op
    in zip(tensor_list, stored_list, maybe_shared_map_ops)]
# Expand dims of stored tensors by 1 for proper enqueue shape
stored_list = [
    array_ops.expand_dims(s, [-1]) if s_info.sparse else s
    for s, s_info in zip(stored_list, sparse_info_list)]
exit((stored_list, sparse_info_list))
