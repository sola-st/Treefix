# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, r'Parse config.*already exists'):
    fc._weighted_categorical_column(
        categorical_column=fc._categorical_column_with_identity(
            key='aaa', num_buckets=3),
        weight_feature_key='aaa')._parse_example_spec()
