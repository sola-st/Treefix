# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
original = fc._categorical_column_with_identity(key='aaa', num_buckets=3)
for column in (original, copy.deepcopy(original)):
    self.assertEqual('aaa', column.name)
    self.assertEqual(3, column._num_buckets)
    self.assertEqual({
        'aaa': parsing_ops.VarLenFeature(dtypes.int64)
    }, column._parse_example_spec)
