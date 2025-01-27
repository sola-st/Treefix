# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError,
                            'hash_bucket_size must be at least 1'):
    fc._categorical_column_with_hash_bucket('aaa', 0)
