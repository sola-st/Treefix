# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_checkpoint_test.py
self._initializer = initializer
self._rows = rows

table = tpu_embedding_v2_utils.TableConfig(
    vocabulary_size=self._rows,
    dim=4,
    initializer=self._initializer,
    combiner='sum',
    name='table')
feature_config = (tpu_embedding_v2_utils.FeatureConfig(
    table=table, name='feature'),)
optimizer = tpu_embedding_v2_utils.SGD()

self.tpu_embedding = tpu_embedding_v2.TPUEmbedding(
    feature_config, optimizer)
