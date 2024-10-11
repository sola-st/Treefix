# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError, 'key must be a string.'):
    fc.numeric_column(key=('aaa',))
