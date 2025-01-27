# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column('aaa')
self.assertEqual('aaa', a.key)
self.assertEqual('aaa', a.name)
self.assertEqual('aaa', a._var_scope_name)
self.assertEqual((1,), a.shape)
self.assertIsNone(a.default_value)
self.assertEqual(dtypes.float32, a.dtype)
self.assertIsNone(a.normalizer_fn)
