# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', default_value=4.)
self.assertEqual((4.,), a.default_value)
a = fc.numeric_column('aaa', shape=[1, 2], default_value=[[3, 2.]])
self.assertEqual(((3., 2.),), a.default_value)
