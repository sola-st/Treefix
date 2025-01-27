# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', shape=[2])
a_bucketized = fc.bucketized_column(a, boundaries=[0, 1])
a_bucketized_copy = copy.deepcopy(a_bucketized)
self.assertEqual(a_bucketized_copy.name, 'aaa_bucketized')
self.assertAllEqual(a_bucketized_copy.variable_shape, (2, 3))
self.assertEqual(a_bucketized_copy.boundaries, (0, 1))
