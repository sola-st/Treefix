# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError,
                            'dtype must be convertible to float'):
    fc.numeric_column('aaa', dtype=dtypes.string)
