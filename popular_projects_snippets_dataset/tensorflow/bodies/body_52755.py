# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, r'Parse config.*already exists'):
    fc.weighted_categorical_column(
        categorical_column=fc.categorical_column_with_identity(
            key='aaa', num_buckets=3),
        weight_feature_key='aaa').parse_example_spec()
