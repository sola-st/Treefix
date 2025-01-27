# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization_test.py

class NotAFeatureColumn(object):
    pass

with self.assertRaisesRegex(ValueError, 'is not a FeatureColumn'):
    serialization.serialize_feature_column(NotAFeatureColumn())
