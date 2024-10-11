# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column('aaa', shape=[2, 3], dtype=dtypes.int32)
self.assertEqual({
    'aaa': parsing_ops.FixedLenFeature((2, 3), dtype=dtypes.int32)
}, a._parse_example_spec)
