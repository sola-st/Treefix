# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', shape=[2], dtype=dtypes.int32)
b = fc.bucketized_column(a, boundaries=[0, 1])
# Column 'aaa` has shape [2] times three buckets -> variable_shape=[2, 3].
self.assertAllEqual((2, 3), b.variable_shape)
