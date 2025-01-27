# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'Duplicate keys'):
    fc.categorical_column_with_vocabulary_list(
        key='aaa', vocabulary_list=(12, 24, 12))
