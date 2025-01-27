# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(
    ValueError, 'Expected feature_columns to be iterable, found dict.'):
    fc.linear_model(
        features={'a': [[0]]}, feature_columns={'a': fc._numeric_column('a')})
