# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
mid_level = self._create_mid_level()
features = self._get_ragged_tensors()
weights = self._get_ragged_tensors(dtype=dtypes.float32)
results = mid_level(features, weights=weights)
weighted_sum = []
for feature, weight, config in zip(nest.flatten(features),
                                   nest.flatten(weights),
                                   self.feature_config):
    table = mid_level.embedding_tables[config.table].numpy()
    # Expand dims here needed to broadcast this multiplication properly.
    weight = np.expand_dims(weight.values.numpy(), axis=1)
    all_lookups = table[feature.values.numpy()] * weight
    row_starts = feature.row_starts().numpy()
    weighted_sum.append(np.add.reduceat(all_lookups, row_starts))
    if config.table.combiner == 'mean':
        weighted_sum[-1] /= np.add.reduceat(weight, row_starts)
self.assertAllClose(results, nest.pack_sequence_as(results,
                                                   weighted_sum))
