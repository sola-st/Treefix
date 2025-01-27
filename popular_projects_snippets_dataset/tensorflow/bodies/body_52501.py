# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(
    ValueError, 'Expected feature_columns to be iterable, found dict.'):
    fc_old.linear_model(
        features={'a': [[0]]}, feature_columns={'a': fc.numeric_column('a')})
