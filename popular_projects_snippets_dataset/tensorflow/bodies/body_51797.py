# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column('aaa')
with self.assertRaisesRegex(ValueError, 'boundaries must be a sorted list'):
    fc._bucketized_column(a, boundaries=None)
with self.assertRaisesRegex(ValueError, 'boundaries must be a sorted list'):
    fc._bucketized_column(a, boundaries=1.)
with self.assertRaisesRegex(ValueError, 'boundaries must be a sorted list'):
    fc._bucketized_column(a, boundaries=[1, 0])
with self.assertRaisesRegex(ValueError, 'boundaries must be a sorted list'):
    fc._bucketized_column(a, boundaries=[1, 1])
