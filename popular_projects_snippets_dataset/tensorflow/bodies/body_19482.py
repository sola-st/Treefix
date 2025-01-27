# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_optimizer_test.py
with self.assertRaisesRegex(
    ValueError, 'is an unsupported optimizer class.'):
    with self._get_strategy().scope():
        tpu_embedding_v2.TPUEmbedding(
            self.feature_config,
            tpu_embedding.AdagradParameters(learning_rate=0.1))
