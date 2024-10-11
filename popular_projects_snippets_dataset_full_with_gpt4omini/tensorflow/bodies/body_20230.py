# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
feature_config = (tpu_embedding_v2_utils.FeatureConfig(
    table=self.table_user, name='friends', max_sequence_length=2),)
optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
embedding_one = tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config=feature_config, optimizer=optimizer)
embedding_two = tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config=feature_config, optimizer=optimizer)

# Both of the tpu embedding tables should be able to build on cpu.
embedding_one.build()
embedding_two.build()
