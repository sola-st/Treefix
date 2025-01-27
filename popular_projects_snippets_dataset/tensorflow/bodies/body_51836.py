# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError, 'Unsupported key type'):
    fc._crossed_column(['a', fc._numeric_column('c')], 10)

with self.assertRaisesRegex(
    ValueError, 'categorical_column_with_hash_bucket is not supported'):
    fc._crossed_column(
        ['a', fc._categorical_column_with_hash_bucket('c', 10)], 10)
