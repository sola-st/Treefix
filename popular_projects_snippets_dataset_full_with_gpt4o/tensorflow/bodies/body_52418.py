# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('aaa', shape=[1, 2], default_value=[[3., 2.]])
a_copy = copy.deepcopy(a)
self.assertEqual(a_copy.name, 'aaa')
self.assertEqual(a_copy.shape, (1, 2))
self.assertEqual(a_copy.default_value, ((3., 2.),))
