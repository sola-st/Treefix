# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('a', dtype=dtypes.int32)
b = fc.bucketized_column(a, boundaries=[0, 1])
crossed1 = fc.crossed_column(['d1', 'd2'], 10)
crossed2 = fc.crossed_column([b, 'c', crossed1], 15, hash_key=5)
crossed2_copy = copy.deepcopy(crossed2)
self.assertEqual(
    'a_bucketized_X_c_X_d1_X_d2',
    crossed2_copy.name,
)
self.assertEqual(15, crossed2_copy.hash_bucket_size)
self.assertEqual(5, crossed2_copy.hash_key)
