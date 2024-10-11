# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_identity(key='aaa', num_buckets=3)
self.assertEqual('aaa', column.name)
self.assertEqual('aaa', column.key)
self.assertEqual(3, column.num_buckets)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.int64)
}, column.parse_example_spec)
self.assertTrue(column._is_v2_column)
