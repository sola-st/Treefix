# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._categorical_column_with_hash_bucket('aaa', 10, dtype=dtypes.int32)
self.assertEqual({
    'aaa': parsing_ops.VarLenFeature(dtypes.int32)
}, a._parse_example_spec)
