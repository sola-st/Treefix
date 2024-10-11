# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column('aaa', dtype=dtypes.int32)
b = fc._bucketized_column(a, boundaries=[0, 1])
self.assertEqual('aaa_bucketized', b.name)
