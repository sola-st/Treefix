# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
with self.assertRaisesRegex(TypeError, 'shape dimensions must be integer'):
    sfc.sequence_numeric_column('aaa', shape=[1.0])

with self.assertRaisesRegex(ValueError,
                            'shape dimensions must be greater than 0'):
    sfc.sequence_numeric_column('aaa', shape=[0])
