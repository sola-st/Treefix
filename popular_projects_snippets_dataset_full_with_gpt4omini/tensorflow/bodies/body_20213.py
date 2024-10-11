# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
mid_level = self._create_mid_level()
features = self._get_dense_tensors()
results = mid_level(features, weights=None)
all_lookups = []
for feature, config in zip(nest.flatten(features), self.feature_config):
    table = mid_level.embedding_tables[config.table].numpy()
    all_lookups.append(table[feature.numpy()])
self.assertAllClose(results, nest.pack_sequence_as(results, all_lookups))
