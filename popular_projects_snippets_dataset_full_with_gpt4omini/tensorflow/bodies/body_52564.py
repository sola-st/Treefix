# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(
    ValueError, 'Duplicate feature column name found for columns'):
    fc_old.input_layer(
        features={'a': [[0]]},
        feature_columns=[fc.numeric_column('a'),
                         fc.numeric_column('a')])
