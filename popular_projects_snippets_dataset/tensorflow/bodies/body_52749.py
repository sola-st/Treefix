# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.weighted_categorical_column(
    categorical_column=fc.categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
self.assertEqual('ids_weighted_by_values', column.name)
self.assertEqual(3, column.num_buckets)
self.assertEqual({
    'ids': parsing_ops.VarLenFeature(dtypes.int64),
    'values': parsing_ops.VarLenFeature(dtypes.float32)
}, column.parse_example_spec)
self.assertTrue(column._is_v2_column)
