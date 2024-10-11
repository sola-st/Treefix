# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._categorical_column_with_vocabulary_file(
    key='aaa', vocabulary_file='path_to_file', vocabulary_size=3)
self.assertEqual('aaa', column.name)
self.assertEqual('aaa', column._var_scope_name)
self.assertEqual('aaa', column.key)
self.assertEqual(3, column._num_buckets)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.string)
}, column._parse_example_spec)
