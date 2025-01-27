# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
dtype = dtypes_lib.qint16
z = array_ops.zeros([2, 3], dtype=dtype)
self.assertEqual(z.dtype, dtype)
self.assertEqual([2, 3], z.get_shape())
# cast to int32 so that it can be compred with numpy
# where [qint|quint][8|16] are not available.
z_value = self.evaluate(math_ops.cast(z, dtypes_lib.int32))
self.assertFalse(np.any(z_value))
