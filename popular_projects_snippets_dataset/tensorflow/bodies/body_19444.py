# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
sparse_features = (
    sparse_tensor.SparseTensor(
        indices=self.feature_watched_indices_high_dimensional,
        values=self.feature_watched_values_high_dimensional,
        dense_shape=[self.data_batch_size, self.data_batch_size, 2]),
    sparse_tensor.SparseTensor(
        indices=self.feature_favorited_indices_high_dimensional,
        values=self.feature_favorited_values_high_dimensional,
        dense_shape=[self.data_batch_size, self.data_batch_size, 2]),
    sparse_tensor.SparseTensor(
        indices=self.feature_friends_indices_high_dimensional,
        values=self.feature_friends_values_high_dimensional,
        dense_shape=[self.data_batch_size, self.data_batch_size, 3]))
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

dataset = dataset_ops.DatasetV2.from_tensors(sparse_features)
# Data is batched to self.data_batch_size, rebatch to global batch size.
exit(dataset.unbatch().repeat().batch(
    self.batch_size * strategy.num_replicas_in_sync, drop_remainder=True))
