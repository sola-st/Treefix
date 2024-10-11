# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column('aaa', shape=[2], dtype=dtypes.int32)
b = fc._bucketized_column(a, boundaries=[0, 1])
# Column 'aaa` has shape [2] times three buckets -> num_buckets=6.
self.assertEqual(6, b._num_buckets)
