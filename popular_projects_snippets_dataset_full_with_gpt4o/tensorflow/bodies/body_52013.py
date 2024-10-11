# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'dtype must be string or integer'):
    fc._categorical_column_with_vocabulary_file(
        key='aaa',
        vocabulary_file='path',
        vocabulary_size=3,
        dtype=dtypes.float64)
