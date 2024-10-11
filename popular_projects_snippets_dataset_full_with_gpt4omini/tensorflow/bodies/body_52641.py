# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'Invalid num_oov_buckets'):
    fc.categorical_column_with_vocabulary_list(
        key='aaa', vocabulary_list=(12, 24, 36), num_oov_buckets=-1)
