# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
fc._categorical_column_with_hash_bucket('aaa', 10, dtype=dtypes.string)
fc._categorical_column_with_hash_bucket('aaa', 10, dtype=dtypes.int32)
with self.assertRaisesRegex(ValueError, 'dtype must be string or integer'):
    fc._categorical_column_with_hash_bucket('aaa', 10, dtype=dtypes.float32)
