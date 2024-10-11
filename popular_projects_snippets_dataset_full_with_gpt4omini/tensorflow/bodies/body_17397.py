# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Internal implementation for sparse_merge to avoid deprecation warnings."""
if isinstance(sp_ids, sparse_tensor.SparseTensorValue) or isinstance(
    sp_ids, sparse_tensor.SparseTensor):
    sp_ids = [sp_ids]
    if not (isinstance(vocab_size, ops.Tensor) or
            isinstance(vocab_size, numbers.Integral)):
        raise TypeError("vocab_size has to be a Tensor or Python int. Found %s" %
                        type(vocab_size))
    vocab_size = [vocab_size]
else:
    if not isinstance(sp_ids, collections_abc.Iterable):
        raise TypeError("sp_ids has to be a SparseTensor or list thereof. "
                        "Found %s" % type(sp_ids))
    if not isinstance(vocab_size, collections_abc.Iterable):
        raise TypeError("vocab_size has to be a list of Tensors or Python ints. "
                        "Found %s" % type(vocab_size))
    for dim in vocab_size:
        if not (isinstance(dim, ops.Tensor) or isinstance(dim, numbers.Integral)):
            raise TypeError(
                "vocab_size has to be a list of Tensors or Python ints. Found %s" %
                type(dim))
if len(sp_ids) != len(vocab_size):
    raise ValueError("sp_ids and vocab_size have to have equal lengths.")

with ops.name_scope(name, "SparseMerge", [sp_ids, sp_values]):
    sp_ids = [_convert_to_sparse_tensor(sp_ids_dim) for sp_ids_dim in sp_ids]
    sp_values = _convert_to_sparse_tensor(sp_values)
    ids = []
    for sp_ids_dim in sp_ids:
        ids_dim = sp_ids_dim.values
        if sp_ids_dim.dtype != dtypes.int64:
            ids_dim = math_ops.cast(ids_dim, dtypes.int64)
        ids += [array_ops.expand_dims(ids_dim, axis=1)]

    vocab_size = [math_ops.cast(x, dtypes.int64) for x in vocab_size]

    # Slice off the last dimension of indices, then tack on the ids
    indices_columns_to_preserve = sp_ids[0].indices[:, :-1]
    new_indices = array_ops.concat([indices_columns_to_preserve] + ids, 1)

    new_values = sp_values.values
    new_shape = array_ops.concat([sp_ids[0].dense_shape[:-1], vocab_size], 0)

    result = sparse_tensor.SparseTensor(new_indices, new_values, new_shape)
    if already_sorted:
        exit(result)
    sorted_result = sparse_reorder(result)
    exit(sparse_tensor.SparseTensor(
        sorted_result.indices, sorted_result.values, new_shape))
