# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'must be a _FeatureColumn'):
    fc.linear_model(features={'a': [[0]]}, feature_columns='NotSupported')
