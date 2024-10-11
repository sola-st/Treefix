# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', shape=[2, 3])
with self.assertRaisesRegex(ValueError,
                            'source_column must be one-dimensional column'):
    fc.bucketized_column(a, boundaries=[0, 1])
