# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column('aaa', shape=[2], dtype=dtypes.int32)
b = fc._bucketized_column(a, boundaries=[0, 1])
self.assertEqual({
    'aaa': parsing_ops.FixedLenFeature((2,), dtype=dtypes.int32)
}, b._parse_example_spec)
