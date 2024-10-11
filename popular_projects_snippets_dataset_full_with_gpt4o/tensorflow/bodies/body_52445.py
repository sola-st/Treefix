# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'hash_bucket_size must be set.'):
    fc.categorical_column_with_hash_bucket('aaa', None)
