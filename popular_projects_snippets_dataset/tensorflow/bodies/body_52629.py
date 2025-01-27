# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_vocabulary_list(
    key='aaa', vocabulary_list=('omar', 'stringer', 'marlo'))
self.assertEqual('aaa', column.name)
self.assertEqual('aaa', column.key)
self.assertEqual(3, column.num_buckets)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.string)
}, column.parse_example_spec)
self.assertTrue(column._is_v2_column)
