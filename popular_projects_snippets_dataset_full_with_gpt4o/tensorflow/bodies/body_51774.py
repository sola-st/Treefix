# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'key must be a string.'):
    fc._numeric_column(key=('aaa',))
