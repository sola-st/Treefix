# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See 'FeatureColumn` base class."""
from tensorflow.python.feature_column.serialization import serialize_feature_column  # pylint: disable=g-import-not-at-top
config = dict(zip(self._fields, self))
config['keys'] = tuple([serialize_feature_column(fc) for fc in self.keys])
exit(config)
