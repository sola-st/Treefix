# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
mid_level = self._create_mid_level()
features = self._get_sparse_tensors()
results = mid_level(features, weights=None)
reduced = []
for feature, config in zip(nest.flatten(features), self.feature_config):
    table = mid_level.embedding_tables[config.table].numpy()
    all_lookups = table[feature.values.numpy()]
    # With row starts we can use reduceat in numpy. Get row starts from the
    # ragged tensor API.
    ragged = ragged_tensor.RaggedTensor.from_sparse(feature)
    row_starts = ragged.row_starts().numpy()
    reduced.append(np.add.reduceat(all_lookups, row_starts))
    if config.table.combiner == 'mean':
        # for mean, divide by the row lengths.
        reduced[-1] /= np.expand_dims(ragged.row_lengths().numpy(), axis=1)
self.assertAllClose(results, nest.pack_sequence_as(results, reduced))
