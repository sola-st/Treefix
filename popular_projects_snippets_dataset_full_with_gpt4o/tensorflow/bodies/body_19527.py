# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_initialization_test.py
feature_config = tpu_embedding_v2_utils.FeatureConfig(
    table=self.table_user, name='friends', max_sequence_length=2)
optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
strategy = self._get_strategy()
with strategy.scope():
    embedding_one = tpu_embedding_v2.TPUEmbedding(
        feature_config=feature_config, optimizer=optimizer)
    embedding_two = tpu_embedding_v2.TPUEmbedding(
        feature_config=feature_config, optimizer=optimizer)

# The first TPU embedding should be able to be built.
# The second one should fail with a runtime error indicating another TPU
# embedding has already been initialized on TPU.
embedding_one.build(64)
with self.assertRaisesRegex(RuntimeError,
                            'TPU is already initialized for embeddings.'):
    embedding_two.build(64)
