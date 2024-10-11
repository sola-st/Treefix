# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._categorical_column_with_hash_bucket('aaa', 10)
self.assertEqual('aaa', a.name)
self.assertEqual('aaa', a._var_scope_name)
self.assertEqual('aaa', a.key)
self.assertEqual(10, a.hash_bucket_size)
self.assertEqual(dtypes.string, a.dtype)
