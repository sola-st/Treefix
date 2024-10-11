# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
sparse_features = (sparse_tensor.SparseTensor(
    indices=self.feature_watched_indices,
    values=self.feature_watched_values,
    dense_shape=[self.data_batch_size, 2]),
                   sparse_tensor.SparseTensor(
                       indices=self.feature_favorited_indices,
                       values=self.feature_favorited_values,
                       dense_shape=[self.data_batch_size, 2]),
                   sparse_tensor.SparseTensor(
                       indices=self.feature_friends_indices,
                       values=self.feature_friends_values,
                       dense_shape=[self.data_batch_size, 3]))
if include_weights:
    weights = []
    for sparse in sparse_features:
        values = (
            array_ops.ones_like(sparse.values, dtype=dtypes.float32) * weight)
        weights.append(
            sparse_tensor.SparseTensor(
                indices=sparse.indices,
                values=values,
                dense_shape=sparse.dense_shape))
    sparse_features = (sparse_features, tuple(weights))
exit(sparse_features)
