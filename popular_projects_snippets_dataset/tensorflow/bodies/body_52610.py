# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'Invalid num_oov_buckets'):
    fc.categorical_column_with_vocabulary_file(
        key='aaa',
        vocabulary_file='path',
        vocabulary_size=3,
        num_oov_buckets=-1)
