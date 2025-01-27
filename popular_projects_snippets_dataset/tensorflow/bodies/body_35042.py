# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = constant_op.constant(2, dtype=dtypes.int32)
self.assertEqual(np.array(2, dtype=np.int32), du.maybe_get_static_value(x))
self.assertAllClose(
    np.array(2.), du.maybe_get_static_value(x, dtype=np.float64))
