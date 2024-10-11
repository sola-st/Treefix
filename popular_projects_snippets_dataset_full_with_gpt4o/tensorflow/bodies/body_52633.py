# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
original = fc.categorical_column_with_vocabulary_list(
    key='aaa', vocabulary_list=(12, 24, 36), dtype=dtypes.int32)
for column in (original, copy.deepcopy(original)):
    self.assertEqual('aaa', column.name)
    self.assertEqual(3, column.num_buckets)
    self.assertEqual({
        'aaa': parsing_ops.VarLenFeature(dtypes.int32)
    }, column.parse_example_spec)
