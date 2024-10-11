# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
fc._numeric_column(
    'aaa', shape=[2], default_value=[1, 2.], dtype=dtypes.float32)
fc._numeric_column(
    'aaa', shape=[2], default_value=[1, 2], dtype=dtypes.int32)
with self.assertRaisesRegex(TypeError, 'must be compatible with dtype'):
    fc._numeric_column(
        'aaa', shape=[2], default_value=[1, 2.], dtype=dtypes.int32)
with self.assertRaisesRegex(TypeError,
                            'default_value must be compatible with dtype'):
    fc._numeric_column('aaa', default_value=['string'])
