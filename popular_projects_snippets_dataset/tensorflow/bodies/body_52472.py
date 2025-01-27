# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('a', shape=[2], dtype=dtypes.int32)
b = fc.bucketized_column(a, boundaries=[0, 1])
crossed = fc.crossed_column([b, 'c'], 15)
self.assertEqual(15, crossed.num_buckets)
