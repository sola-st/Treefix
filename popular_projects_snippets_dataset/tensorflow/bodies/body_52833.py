# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See 'FeatureColumn` base class."""
config = dict(zip(self._fields, self))
from tensorflow.python.feature_column import serialization  # pylint: disable=g-import-not-at-top
config['normalizer_fn'] = serialization._serialize_keras_object(  # pylint: disable=protected-access
    self.normalizer_fn)
config['dtype'] = self.dtype.name
exit(config)
