# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', dtype=dtypes.int32)
b = fc.bucketized_column(a, boundaries=[0, 1])
self.assertTrue(b._is_v2_column)
self.assertEqual('aaa_bucketized', b.name)
