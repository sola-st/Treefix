# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'is not convertible to float'):
    fc.weighted_categorical_column(
        categorical_column=fc.categorical_column_with_identity(
            key='ids', num_buckets=3),
        weight_feature_key='values',
        dtype=None)
