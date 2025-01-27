# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError,
                            'feature_columns must not be empty'):
    fc_old.input_layer(features={}, feature_columns=[])
