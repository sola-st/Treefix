# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa')
self.assertEqual('aaa', a.key)
self.assertEqual('aaa', a.name)
self.assertEqual((1,), a.shape)
self.assertIsNone(a.default_value)
self.assertEqual(dtypes.float32, a.dtype)
self.assertIsNone(a.normalizer_fn)
self.assertTrue(a._is_v2_column)
