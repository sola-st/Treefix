# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'hash_bucket_size must be > 1'):
    fc._crossed_column(['a', 'c'], 0)
