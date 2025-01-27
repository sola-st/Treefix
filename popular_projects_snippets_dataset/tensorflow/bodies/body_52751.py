# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
"""Tests deepcopy of categorical_column_with_hash_bucket."""
original = fc.weighted_categorical_column(
    categorical_column=fc.categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
for column in (original, copy.deepcopy(original)):
    self.assertEqual('ids_weighted_by_values', column.name)
    self.assertEqual(3, column.num_buckets)
    self.assertEqual({
        'ids': parsing_ops.VarLenFeature(dtypes.int64),
        'values': parsing_ops.VarLenFeature(dtypes.float32)
    }, column.parse_example_spec)
