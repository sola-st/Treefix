# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
feature_config = (
    tpu_embedding_v2_utils.FeatureConfig(
        table=self.table_video, name='watched', max_sequence_length=2),)
mid_level = tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config=feature_config, optimizer=None)
# Build the layer manually to create the variables. Normally calling enqueue
# would do this.
mid_level.build()
self.assertEqual(
    list(mid_level._variables[self.table_video.name].keys()),
    ['parameters'])
