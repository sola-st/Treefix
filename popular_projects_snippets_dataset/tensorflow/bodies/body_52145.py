# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._weighted_categorical_column(
    categorical_column=fc._categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
self.assertEqual('ids_weighted_by_values', column.name)
self.assertEqual('ids_weighted_by_values', column._var_scope_name)
self.assertEqual(3, column._num_buckets)
self.assertEqual({
    'ids': parsing_ops.VarLenFeature(dtypes.int64),
    'values': parsing_ops.VarLenFeature(dtypes.float32)
}, column._parse_example_spec)
