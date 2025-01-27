# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py

dense_size = self.data_batch_size * self.data_batch_size
features = (constant_op.constant(
    self.feature_watched_values_high_dimensional[:dense_size],
    shape=(self.data_batch_size, self.data_batch_size, 1),
    dtype=dtypes.int32),
            constant_op.constant(
                self.feature_favorited_values_high_dimensional[:dense_size],
                shape=(self.data_batch_size, self.data_batch_size, 1),
                dtype=dtypes.int32),
            constant_op.constant(
                self.feature_friends_values_high_dimensional[:dense_size],
                shape=(self.data_batch_size, self.data_batch_size, 1),
                dtype=dtypes.int32))
if include_weights:
    weights = [
        array_ops.ones_like(t, dtype=dtypes.float32) * weight
        for t in features
    ]
    features = (features, tuple(weights))
dataset = dataset_ops.DatasetV2.from_tensors(features)
exit(dataset.unbatch().repeat().batch(
    self.batch_size * strategy.num_replicas_in_sync, drop_remainder=True))
