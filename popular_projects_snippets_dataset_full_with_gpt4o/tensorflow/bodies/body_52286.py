# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
feature_tensors = []
for key in _collect_leaf_level_keys(self):
    if isinstance(key, six.string_types):
        feature_tensors.append(inputs.get(key))
    elif isinstance(key, _CategoricalColumn):
        ids_and_weights = key._get_sparse_tensors(inputs)  # pylint: disable=protected-access
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
