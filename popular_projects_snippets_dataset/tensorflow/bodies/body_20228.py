# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
# Prod of output shape is not a factor of the data batch size.
# An error will be raised in this case.
feature_config = (tpu_embedding_v2_utils.FeatureConfig(
    table=self.table_user, name='friends', output_shape=[3]),)
optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
mid_level = tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config=feature_config, optimizer=optimizer)
features = self._get_ragged_tensors()[2:3]
with self.assertRaisesRegex(
    ValueError,
    'Output shape set in the FeatureConfig should be the factor'):
    mid_level(features, weights=None)
