# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(
    ValueError, 'Duplicate feature column name found for columns'):
    get_keras_linear_model_predictions(
        features={'a': [[0]]},
        feature_columns=[fc._numeric_column('a'),
                         fc._numeric_column('a')])
