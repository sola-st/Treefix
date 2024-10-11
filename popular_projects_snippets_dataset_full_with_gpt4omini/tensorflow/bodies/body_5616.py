# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable([1., 2., 3.])
self.assertEqual(v[1], 2.)
v[2].assign(4.)
self.assertAllEqual(v, [1., 2., 4.])
