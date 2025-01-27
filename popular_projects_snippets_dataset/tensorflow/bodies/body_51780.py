# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError,
                            'dtype must be convertible to float'):
    fc._numeric_column('aaa', dtype=dtypes.string)
