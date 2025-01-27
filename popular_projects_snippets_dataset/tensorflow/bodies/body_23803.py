# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
x = np.array([[1, 2, 3]], dtype=float_type)
self.assertEqual(float_type, x.dtype)
self.assertEqual("[[1 2 3]]", str(x))
np.testing.assert_equal(x, x)
numpy_assert_allclose(x, x, float_type=float_type)
self.assertTrue((x == x).all())
