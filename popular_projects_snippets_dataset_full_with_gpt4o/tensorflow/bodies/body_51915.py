# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError,
                            'feature_columns must not be empty'):
    get_keras_linear_model_predictions(features={}, feature_columns=[])
