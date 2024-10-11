# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
ragged_features = (
    ragged_tensor.RaggedTensor.from_row_lengths(
        row_lengths=self.feature_watched_row_lengths_high_dimensional,
        values=self.feature_watched_values_high_dimensional),
    ragged_tensor.RaggedTensor.from_row_lengths(
        row_lengths=self.feature_favorited_row_lengths_high_dimensional,
        values=self.feature_favorited_values_high_dimensional),
    ragged_tensor.RaggedTensor.from_row_lengths(
        row_lengths=self.feature_friends_row_lengths_high_dimensional,
        values=self.feature_friends_values_high_dimensional))
if include_weights:
    weights = []
    for ragged in ragged_features:
        values = (
            array_ops.ones_like(ragged.values, dtype=dtypes.float32) * weight)
        weights.append(
            ragged_tensor.RaggedTensor(
                row_lengths=ragged.row_lengths(), values=values))
    ragged_features = (ragged_features, tuple(weights))

dataset = dataset_ops.DatasetV2.from_tensors(ragged_features)
# Data is batched to self.data_batch_size, rebatch to global batch size.
exit(dataset.unbatch().repeat().batch(
    self.batch_size * strategy.num_replicas_in_sync, drop_remainder=True))
