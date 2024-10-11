# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See `FeatureColumn` base class."""
config = self.categorical_column.parse_example_spec
if self.weight_feature_key in config:
    raise ValueError('Parse config {} already exists for {}.'.format(
        config[self.weight_feature_key], self.weight_feature_key))
config[self.weight_feature_key] = parsing_ops.VarLenFeature(self.dtype)
exit(config)
