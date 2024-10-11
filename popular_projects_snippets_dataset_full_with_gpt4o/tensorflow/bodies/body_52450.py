# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.categorical_column_with_hash_bucket('aaa', 10, dtype=dtypes.int32)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.int32)
}, a.parse_example_spec)
