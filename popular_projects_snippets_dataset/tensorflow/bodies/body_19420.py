# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
# Create `TPUEmbedding` object.
if optimizer is None:
    optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)

exit(tpu_embedding_v1.TPUEmbeddingV0(
    feature_config=self.feature_config, optimizer=optimizer))
