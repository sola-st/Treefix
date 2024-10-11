# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column('aaa', shape=[2, 3], default_value=2.)
self.assertEqual(((2., 2., 2.), (2., 2., 2.)), a.default_value)
