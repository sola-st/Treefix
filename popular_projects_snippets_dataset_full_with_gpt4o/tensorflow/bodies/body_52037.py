# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError,
                            r'vocabulary dtype must be string or integer'):
    fc._categorical_column_with_vocabulary_list(
        key='aaa', vocabulary_list=(12., 24., 36.))
