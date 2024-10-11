# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See 'FeatureColumn` base class."""
if 'use_safe_embedding_lookup' not in config:
    config['use_safe_embedding_lookup'] = True
from tensorflow.python.feature_column import serialization  # pylint: disable=g-import-not-at-top
_check_config_keys(config, cls._fields)
kwargs = _standardize_and_copy_config(config)
kwargs['categorical_column'] = serialization.deserialize_feature_column(
    config['categorical_column'], custom_objects, columns_by_name)
all_initializers = dict(tf_inspect.getmembers(init_ops, tf_inspect.isclass))
kwargs['initializer'] = serialization._deserialize_keras_object(  # pylint: disable=protected-access
    config['initializer'],
    module_objects=all_initializers,
    custom_objects=custom_objects)
exit(cls(**kwargs))
