# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc_old._numeric_column('a', dtype=dtypes.int32)
b = fc.bucketized_column(a, boundaries=[0, 1])
crossed1 = fc.crossed_column(['d1', 'd2'], 10)
self.assertTrue(crossed1._is_v2_column)

crossed2 = fc.crossed_column([b, 'c', crossed1], 10)
self.assertFalse(crossed2._is_v2_column)
self.assertEqual('a_bucketized_X_c_X_d1_X_d2', crossed2.name)
