# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See 'FeatureColumn` base class."""
_check_config_keys(config, cls._fields)
kwargs = _standardize_and_copy_config(config)
exit(cls(**kwargs))
