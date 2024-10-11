# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._categorical_column_with_vocabulary_file(
    key='aaa',
    vocabulary_file='path_to_file',
    vocabulary_size=3,
    num_oov_buckets=4,
    dtype=dtypes.int32)
self.assertEqual(7, column._num_buckets)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.int32)
}, column._parse_example_spec)
