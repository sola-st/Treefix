# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
self.assertEqual(None, du.maybe_get_static_value(x))
self.assertEqual(None, du.maybe_get_static_value(x, dtype=np.float64))
