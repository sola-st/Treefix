# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(ValueError,
                            'keys must be a list with length > 1'):
    fc.crossed_column([], 10)
