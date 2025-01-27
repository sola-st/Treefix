# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError,
                            'feature_columns must not be empty'):
    fc.linear_model(features={}, feature_columns=[])
