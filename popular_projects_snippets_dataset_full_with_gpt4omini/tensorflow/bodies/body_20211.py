# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
exit(tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config=self.feature_config, optimizer=optimizer))
