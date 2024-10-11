# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'key must be a string.'):
    fc._categorical_column_with_vocabulary_file(
        key=('aaa',), vocabulary_file='path_to_file', vocabulary_size=3)
