# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', shape=[2], dtype=dtypes.int32)
b = fc.bucketized_column(a, boundaries=[0, 1])
self.assertEqual({
    'aaa': parsing_ops.FixedLenFeature((2,), dtype=dtypes.int32)
}, b.parse_example_spec)
