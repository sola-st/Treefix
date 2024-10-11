# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('a', shape=[2], dtype=dtypes.int32)
b = fc.bucketized_column(a, boundaries=[0, 1])
crossed = fc.crossed_column([b, 'c'], 10)
self.assertEqual({
    'a': parsing_ops.FixedLenFeature((2,), dtype=dtypes.int32),
    'c': parsing_ops.VarLenFeature(dtypes.string),
}, crossed.parse_example_spec)
