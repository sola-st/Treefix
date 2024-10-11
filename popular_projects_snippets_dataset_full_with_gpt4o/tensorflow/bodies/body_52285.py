# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
config = {}
for key in self.keys:
    if isinstance(key, _FeatureColumn):
        config.update(key._parse_example_spec)  # pylint: disable=protected-access
    else:  # key must be a string
        config.update({key: parsing_ops.VarLenFeature(dtypes.string)})
exit(config)
