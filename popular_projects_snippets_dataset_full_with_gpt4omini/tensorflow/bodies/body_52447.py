# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.categorical_column_with_hash_bucket('aaa', 10, dtype=dtypes.string)
b = fc.categorical_column_with_hash_bucket('aaa', 10, dtype=dtypes.int32)
self.assertEqual(dtypes.string, a.dtype)
self.assertEqual(dtypes.int32, b.dtype)

with self.assertRaisesRegex(ValueError, 'dtype must be string or integer'):
    fc.categorical_column_with_hash_bucket('aaa', 10, dtype=dtypes.float32)
