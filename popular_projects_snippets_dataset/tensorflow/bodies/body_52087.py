# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._categorical_column_with_hash_bucket('a', 4)
indicator_a = fc._indicator_column(a)
self.assertEqual(indicator_a.categorical_column.name, 'a')
self.assertEqual(indicator_a.name, 'a_indicator')
self.assertEqual(indicator_a._var_scope_name, 'a_indicator')
self.assertEqual(indicator_a._variable_shape, [1, 4])

b = fc._categorical_column_with_hash_bucket('b', hash_bucket_size=100)
indicator_b = fc._indicator_column(b)
self.assertEqual(indicator_b.categorical_column.name, 'b')
self.assertEqual(indicator_b.name, 'b_indicator')
self.assertEqual(indicator_b._var_scope_name, 'b_indicator')
self.assertEqual(indicator_b._variable_shape, [1, 100])
