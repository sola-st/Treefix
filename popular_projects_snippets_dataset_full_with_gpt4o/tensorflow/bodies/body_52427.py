# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc_old._numeric_column('aaa', dtype=dtypes.int32)
b = fc.bucketized_column(a, boundaries=[0, 1])
self.assertFalse(b._is_v2_column)
self.assertEqual('aaa_bucketized', b.name)
