# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable([1.])
self.assertEqual(v.shape, (1,))
self.assertEqual(v.get_shape(), (1,))
v.set_shape((1,))
with self.assertRaisesRegex(ValueError, "not compatible"):
    v.set_shape((1, 1))
