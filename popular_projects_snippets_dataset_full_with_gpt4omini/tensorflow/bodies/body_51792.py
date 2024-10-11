# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
a = fc._numeric_column(
    'aaa', shape=[1, 2], default_value=np.array([[3., 2.]]))
self.assertEqual(a.default_value, ((3., 2.),))
