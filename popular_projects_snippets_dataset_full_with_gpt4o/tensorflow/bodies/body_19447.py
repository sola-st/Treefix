# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py

features = (constant_op.constant(
    self.feature_watched_values[:self.data_batch_size], dtype=dtypes.int32),
            constant_op.constant(
                self.feature_favorited_values[:self.data_batch_size],
                dtype=dtypes.int32),
            constant_op.constant(
                self.feature_friends_values[:self.data_batch_size],
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
