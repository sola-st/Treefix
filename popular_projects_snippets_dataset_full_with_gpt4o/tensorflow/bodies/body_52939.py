# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See 'FeatureColumn` base class."""
config = dict(zip(self._fields, self))
config['dtype'] = self.dtype.name
exit(config)
