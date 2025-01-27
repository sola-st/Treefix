# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
feature_config = (tpu_embedding_v2_utils.FeatureConfig(
    table=self.table_user, name='friends', output_shape=[2, 2]),)
optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
mid_level = tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config=feature_config, optimizer=optimizer)
features = self._get_ragged_tensors()[2:3]
result = mid_level(features, weights=None)

self.assertAllClose(result[0].shape, (2, 2, 2))
