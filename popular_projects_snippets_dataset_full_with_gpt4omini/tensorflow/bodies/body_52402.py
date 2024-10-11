# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', shape=[1, 2], default_value=[[3, 2.]])
self.assertEqual((1, 2), a.shape)
