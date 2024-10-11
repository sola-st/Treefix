# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'must be a _FeatureColumn'):
    get_keras_linear_model_predictions(
        features={'a': [[0]]}, feature_columns='NotSupported')
