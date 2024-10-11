# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
"""Creates statically-sized Tensors containing indices and weights.

  From third_party/cloud_tpu/models/movielens/tpu_embedding.py

  Also computes sparse_indices.values % embedding_table_size, for equivalent
  functionality to sparse_column_with_integerized_feature. The returned
  padded weight Tensor also doubles as a mask indicating which values in
  the returned padded indices Tensor are indices versus padded zeros.

  Args:
    sparse_indices: SparseTensor of embedding lookup indices.
    padded_size: Number of columns of the returned Tensors. Indices which fall
      out of bounds will be truncated to the padded size.

  Returns:
    (sparse_indices.values padded to the specified size,
     a mask the same size as the returned padded values in which 0s
     indicate padded locations and 1s (or values from sparse_weights)
     indicate actual values)
  """
batch_size = sparse_indices.dense_shape[0]
sparse_indices = sparse_ops.sparse_slice(sparse_indices, [0, 0],
                                         [batch_size, padded_size])
indices, values = sparse_indices.indices, sparse_indices.values

padded_values = array_ops.scatter_nd(
    indices,
    math_ops.cast(values, dtypes.int32),
    shape=(batch_size, padded_size))

weights = array_ops.ones_like(values, dtype=dtypes.float32)
padded_mask = array_ops.scatter_nd(
    indices, weights, shape=(batch_size, padded_size))

exit((padded_values, padded_mask))
