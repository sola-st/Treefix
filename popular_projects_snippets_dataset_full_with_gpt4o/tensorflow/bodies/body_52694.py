# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.categorical_column_with_hash_bucket('a', 4)
column = fc.indicator_column(a)
column_copy = copy.deepcopy(column)
self.assertEqual(column_copy.categorical_column.name, 'a')
self.assertEqual(column.name, 'a_indicator')
self.assertEqual(column.variable_shape, [1, 4])
