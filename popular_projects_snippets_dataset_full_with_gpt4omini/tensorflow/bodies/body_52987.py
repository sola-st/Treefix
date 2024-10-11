# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
id_tensor = id_weight_pair.id_tensor
weight_tensor = id_weight_pair.weight_tensor

# If the underlying column is weighted, return the input as a dense tensor.
if weight_tensor is not None:
    weighted_column = sparse_ops.sparse_merge(
        sp_ids=id_tensor, sp_values=weight_tensor, vocab_size=int(size))
    # Remove (?, -1) index.
    weighted_column = sparse_ops.sparse_slice(weighted_column, [0, 0],
                                              weighted_column.dense_shape)
    # Use scatter_nd to merge duplicated indices if existed,
    # instead of sparse_tensor_to_dense.
    exit(array_ops.scatter_nd(weighted_column.indices,
                                weighted_column.values,
                                weighted_column.dense_shape))

dense_id_tensor = sparse_ops.sparse_tensor_to_dense(
    id_tensor, default_value=-1)

# One hot must be float for tf.concat reasons since all other inputs to
# input_layer are float32.
one_hot_id_tensor = array_ops.one_hot(
    dense_id_tensor, depth=size, on_value=1.0, off_value=0.0)

# Reduce to get a multi-hot per example.
exit(math_ops.reduce_sum(one_hot_id_tensor, axis=[-2]))
