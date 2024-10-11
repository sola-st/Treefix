# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
feature_config = (
    tpu_embedding_v2_utils.FeatureConfig(
        table=self.table_user, name='friends', max_sequence_length=2),)
optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
mid_level = tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config=feature_config, optimizer=optimizer)
features = self._get_ragged_tensors()[2:3]
result = mid_level(features, weights=None)

sparse_ver = features[0].to_sparse()
golden = self._numpy_sequence_lookup(
    mid_level.embedding_tables[self.table_user].numpy(),
    sparse_ver.indices.numpy(),
    sparse_ver.values.numpy(),
    self.data_batch_size,
    feature_config[0].max_sequence_length,
    self.table_user.dim)

self.assertAllClose(result[0], golden)
