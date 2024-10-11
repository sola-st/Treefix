# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'Missing vocabulary_file'):
    fc.categorical_column_with_vocabulary_file(
        key='aaa', vocabulary_file='', vocabulary_size=3)
