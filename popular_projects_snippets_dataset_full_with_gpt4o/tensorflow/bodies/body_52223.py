# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Returns a `Tensor` for the given key.

    A `str` key is used to access a base feature (not-transformed). When a
    `_FeatureColumn` is passed, the transformed feature is returned if it
    already exists, otherwise the given `_FeatureColumn` is asked to provide its
    transformed output, which is then cached.

    Args:
      key: a `str` or a `_FeatureColumn`.

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

if not isinstance(key, _FeatureColumn):
    raise TypeError('"key" must be either a "str" or "_FeatureColumn". '
                    'Provided: {}'.format(key))

column = key
logging.debug('Transforming feature_column %s.', column)
transformed = column._transform_feature(self)  # pylint: disable=protected-access
if transformed is None:
    raise ValueError('Column {} is not supported.'.format(column.name))
self._feature_tensors[column] = transformed
exit(transformed)
