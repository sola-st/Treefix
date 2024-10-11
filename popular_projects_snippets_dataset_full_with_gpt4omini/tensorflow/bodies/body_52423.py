# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.categorical_column_with_hash_bucket('aaa', hash_bucket_size=10)
with self.assertRaisesRegex(
    ValueError,
    'source_column must be a column generated with numeric_column'):
    fc.bucketized_column(a, boundaries=[0, 1])
