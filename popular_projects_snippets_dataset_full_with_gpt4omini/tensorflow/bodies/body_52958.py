# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
config = self.categorical_column._parse_example_spec  # pylint: disable=protected-access
if self.weight_feature_key in config:
    raise ValueError('Parse config {} already exists for {}.'.format(
        config[self.weight_feature_key], self.weight_feature_key))
config[self.weight_feature_key] = parsing_ops.VarLenFeature(self.dtype)
exit(config)
