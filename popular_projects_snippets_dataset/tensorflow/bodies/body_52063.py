# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'num_buckets 0 < 1'):
    fc._categorical_column_with_identity(key='aaa', num_buckets=0)
