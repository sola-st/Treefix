# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column('a', shape=[2], dtype=dtypes.int32)
b = fc._bucketized_column(a, boundaries=[0, 1])
crossed = fc._crossed_column([b, 'c'], 10)
self.assertEqual({
    'a': parsing_ops.FixedLenFeature((2,), dtype=dtypes.int32),
    'c': parsing_ops.VarLenFeature(dtypes.string),
}, crossed._parse_example_spec)
