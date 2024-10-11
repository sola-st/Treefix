# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization_test.py
with self.assertRaisesRegex(
    ValueError, 'Unknown feature_column_v2: NotExistingFeatureColumnClass'):
    serialization.deserialize_feature_column({
        'class_name': 'NotExistingFeatureColumnClass',
        'config': {}
    })
