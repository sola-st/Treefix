# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
# Create `TPUEmbedding` object.
if optimizer is None:
    optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)

exit(tpu_embedding_v2.TPUEmbedding(
    feature_config=self.feature_config, optimizer=optimizer))
