# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See 'FeatureColumn` base class."""
from tensorflow.python.feature_column import serialization  # pylint: disable=g-import-not-at-top
config = dict(zip(self._fields, self))
config['categorical_column'] = serialization.serialize_feature_column(
    self.categorical_column)
config['initializer'] = serialization._serialize_keras_object(  # pylint: disable=protected-access
    self.initializer)
exit(config)
