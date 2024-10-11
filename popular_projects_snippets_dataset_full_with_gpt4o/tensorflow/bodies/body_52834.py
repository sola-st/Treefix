# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See 'FeatureColumn` base class."""
_check_config_keys(config, cls._fields)
from tensorflow.python.feature_column import serialization  # pylint: disable=g-import-not-at-top
kwargs = _standardize_and_copy_config(config)
kwargs['normalizer_fn'] = serialization._deserialize_keras_object(  # pylint: disable=protected-access
    config['normalizer_fn'],
    custom_objects=custom_objects)
kwargs['dtype'] = dtypes.as_dtype(config['dtype'])

exit(cls(**kwargs))
