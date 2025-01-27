# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError,
                            'both num_oov_buckets and default_value'):
    fc._categorical_column_with_vocabulary_file(
        key='aaa',
        vocabulary_file=self._wire_vocabulary_file_name,
        vocabulary_size=self._wire_vocabulary_size,
        num_oov_buckets=100,
        default_value=2)
