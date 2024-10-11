# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.categorical_column_with_hash_bucket('a', 4)
indicator_a = fc.indicator_column(a)
self.assertEqual(indicator_a.categorical_column.name, 'a')
self.assertEqual(indicator_a.name, 'a_indicator')
self.assertEqual(indicator_a.variable_shape, [1, 4])
self.assertTrue(indicator_a._is_v2_column)

b = fc_old._categorical_column_with_hash_bucket('b', hash_bucket_size=100)
indicator_b = fc.indicator_column(b)
self.assertEqual(indicator_b.categorical_column.name, 'b')
self.assertEqual(indicator_b.name, 'b_indicator')
self.assertEqual(indicator_b.variable_shape, [1, 100])
self.assertFalse(indicator_b._is_v2_column)
