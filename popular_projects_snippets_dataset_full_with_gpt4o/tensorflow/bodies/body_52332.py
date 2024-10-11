# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
a = sfc.sequence_numeric_column('aaa')
self.assertEqual('aaa', a.key)
self.assertEqual('aaa', a.name)
self.assertEqual((1,), a.shape)
self.assertEqual(0., a.default_value)
self.assertEqual(dtypes.float32, a.dtype)
self.assertIsNone(a.normalizer_fn)
