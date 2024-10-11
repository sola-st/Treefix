# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column.py
"""See 'FeatureColumn` base class."""
fc._check_config_keys(config, cls._fields)
kwargs = fc._standardize_and_copy_config(config)
kwargs['dtype'] = dtypes.as_dtype(config['dtype'])
exit(cls(**kwargs))
