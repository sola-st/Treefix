# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
with self.assertRaisesRegex(ValueError,
                            'dtype must be convertible to float'):
    sfc.sequence_numeric_column('aaa', dtype=dtypes.string)
