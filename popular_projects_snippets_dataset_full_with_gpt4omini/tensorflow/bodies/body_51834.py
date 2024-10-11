# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(ValueError,
                            'keys must be a list with length > 1'):
    fc._crossed_column([], 10)
