# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', shape=[2, 3], dtype=dtypes.int32)
self.assertEqual({
    'aaa': parsing_ops.FixedLenFeature((2, 3), dtype=dtypes.int32)
}, a.parse_example_spec)
