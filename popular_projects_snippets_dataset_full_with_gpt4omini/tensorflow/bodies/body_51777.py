# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
fc._numeric_column('aaa', shape=[2], default_value=[1, 2.])
with self.assertRaisesRegex(ValueError, 'The shape of default_value'):
    fc._numeric_column('aaa', shape=[2], default_value=[1, 2, 3.])
fc._numeric_column(
    'aaa', shape=[3, 2], default_value=[[2, 3], [1, 2], [2, 3.]])
with self.assertRaisesRegex(ValueError, 'The shape of default_value'):
    fc._numeric_column(
        'aaa', shape=[3, 1], default_value=[[2, 3], [1, 2], [2, 3.]])
with self.assertRaisesRegex(ValueError, 'The shape of default_value'):
    fc._numeric_column(
        'aaa', shape=[3, 3], default_value=[[2, 3], [1, 2], [2, 3.]])
