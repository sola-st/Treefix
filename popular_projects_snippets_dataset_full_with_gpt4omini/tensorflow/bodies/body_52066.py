# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'default_value 3 not in range'):
    fc._categorical_column_with_identity(
        key='aaa', num_buckets=3, default_value=3)
