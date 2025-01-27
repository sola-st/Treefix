# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'dtype must be string or integer'):
    fc.categorical_column_with_vocabulary_file(
        key='aaa',
        vocabulary_file='path',
        vocabulary_size=3,
        dtype=dtypes.float64)
