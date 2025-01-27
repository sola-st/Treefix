# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'must be a _DenseColumn'):
    fc.input_layer(
        features={'a': [[0]]},
        feature_columns=[
            fc._categorical_column_with_hash_bucket('wire_cast', 4)
        ])
