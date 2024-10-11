# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See `FeatureColumn` base class."""
config = {}
for key in self.keys:
    if isinstance(key, FeatureColumn):
        config.update(key.parse_example_spec)
    elif isinstance(key, fc_old._FeatureColumn):  # pylint: disable=protected-access
        config.update(key._parse_example_spec)  # pylint: disable=protected-access
    else:  # key must be a string
        config.update({key: parsing_ops.VarLenFeature(dtypes.string)})
exit(config)
