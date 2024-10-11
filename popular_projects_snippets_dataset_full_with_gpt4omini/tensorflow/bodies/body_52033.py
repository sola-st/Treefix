# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._categorical_column_with_vocabulary_list(
    key='aaa', vocabulary_list=(12, 24, 36))
self.assertEqual('aaa', column.name)
self.assertEqual('aaa', column.key)
self.assertEqual('aaa', column._var_scope_name)
self.assertEqual(3, column._num_buckets)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.int64)
}, column._parse_example_spec)
