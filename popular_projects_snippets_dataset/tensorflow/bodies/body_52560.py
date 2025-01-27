# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'must be a _DenseColumn'):
    fc_old.input_layer(
        features={'a': [[0]]},
        feature_columns=[
            fc.categorical_column_with_hash_bucket('wire_cast', 4)
        ])
