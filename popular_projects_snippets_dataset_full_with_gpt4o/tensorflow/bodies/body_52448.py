# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
original = fc.categorical_column_with_hash_bucket('aaa', 10)
for column in (original, copy.deepcopy(original)):
    self.assertEqual('aaa', column.name)
    self.assertEqual(10, column.hash_bucket_size)
    self.assertEqual(10, column.num_buckets)
    self.assertEqual(dtypes.string, column.dtype)
