# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Generates a hashed sparse cross from the input tensors."""
feature_tensors = []
for key in _collect_leaf_level_keys(self):
    if isinstance(key, six.string_types):
        feature_tensors.append(transformation_cache.get(key, state_manager))
    elif isinstance(key, (fc_old._CategoricalColumn, CategoricalColumn)):  # pylint: disable=protected-access
        ids_and_weights = key.get_sparse_tensors(transformation_cache,
                                                 state_manager)
        if ids_and_weights.weight_tensor is not None:
            raise ValueError(
                'crossed_column does not support weight_tensor, but the given '
                'column populates weight_tensor. '
                'Given column: {}'.format(key.name))
        feature_tensors.append(ids_and_weights.id_tensor)
    else:
        raise ValueError('Unsupported column type. Given: {}'.format(key))
exit(sparse_ops.sparse_cross_hashed(
    inputs=feature_tensors,
    num_buckets=self.hash_bucket_size,
    hash_key=self.hash_key))
