# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = 2
self.assertEqual(x, du.maybe_get_static_value(x))
self.assertAllClose(
    np.array(2.), du.maybe_get_static_value(x, dtype=np.float64))
