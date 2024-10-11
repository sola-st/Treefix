# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError,
                            r'vocabulary_list.*must be non-empty'):
    fc.categorical_column_with_vocabulary_list(
        key='aaa', vocabulary_list=None)
