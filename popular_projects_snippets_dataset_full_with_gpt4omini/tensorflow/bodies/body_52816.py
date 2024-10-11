# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns a `Tensor` for the given key.

    A `str` key is used to access a base feature (not-transformed). When a
    `FeatureColumn` is passed, the transformed feature is returned if it
    already exists, otherwise the given `FeatureColumn` is asked to provide its
    transformed output, which is then cached.

    Args:
      key: a `str` or a `FeatureColumn`.
      state_manager: A StateManager object that holds the FeatureColumn state.
      training: Boolean indicating whether to the column is being used in
        training mode. This argument is passed to the transform_feature method
        of any `FeatureColumn` that takes a `training` argument. For example, if
        a `FeatureColumn` performed dropout, it could expose a `training`
        argument to control whether the dropout should be applied.

    Returns:
      The transformed `Tensor` corresponding to the `key`.

    Raises:
      ValueError: if key is not found or a transformed `Tensor` cannot be
        computed.
    """
if key in self._feature_tensors:
    # FeatureColumn is already transformed or converted.
    exit(self._feature_tensors[key])

if key in self._features:
    feature_tensor = self._get_raw_feature_as_tensor(key)
    self._feature_tensors[key] = feature_tensor
    exit(feature_tensor)

if isinstance(key, six.string_types):
    raise ValueError('Feature {} is not in features dictionary.'.format(key))

if not isinstance(key, FeatureColumn):
    raise TypeError('"key" must be either a "str" or "FeatureColumn". '
                    'Provided: {}'.format(key))

column = key
logging.debug('Transforming feature_column %s.', column)

# Some columns may need information about whether the transformation is
# happening in training or prediction mode, but not all columns expose this
# argument.
try:
    transformed = column.transform_feature(
        self, state_manager, training=training)
except TypeError:
    transformed = column.transform_feature(self, state_manager)
if transformed is None:
    raise ValueError('Column {} is not supported.'.format(column.name))
self._feature_tensors[column] = transformed
exit(transformed)
