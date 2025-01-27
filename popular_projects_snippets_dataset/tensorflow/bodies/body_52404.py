# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', shape=[2], default_value=[1, 2.])
self.assertEqual((1, 2.), a.default_value)
with self.assertRaisesRegex(ValueError, 'The shape of default_value'):
    fc.numeric_column('aaa', shape=[2], default_value=[1, 2, 3.])
    a = fc.numeric_column(
        'aaa', shape=[3, 2], default_value=[[2, 3], [1, 2], [2, 3.]])
    self.assertEqual(((2, 3), (1, 2), (2, 3.)), a.default_value)
with self.assertRaisesRegex(ValueError, 'The shape of default_value'):
    fc.numeric_column(
        'aaa', shape=[3, 1], default_value=[[2, 3], [1, 2], [2, 3.]])
with self.assertRaisesRegex(ValueError, 'The shape of default_value'):
    fc.numeric_column(
        'aaa', shape=[3, 3], default_value=[[2, 3], [1, 2], [2, 3.]])
