# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/utils.py
if not isinstance(key, six.string_types):
    raise ValueError(
        'key must be a string. Got: type {}. Given key: {}.'.format(
            type(key), key))
