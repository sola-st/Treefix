# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization_test.py
with self.assertRaisesRegex(ValueError, 'Improper config format: {}'):
    serialization.deserialize_feature_column({})
