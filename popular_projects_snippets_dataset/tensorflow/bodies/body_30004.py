# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
d = array_ops.fill([2, 3], 12., name="fill")
self.assertEqual(d.get_shape(), [2, 3])
# Test default type for both constant size and dynamic size
z = array_ops.ones([2, 3])
self.assertEqual(z.dtype, dtypes_lib.float32)
self.assertEqual([2, 3], z.get_shape())
self.assertAllEqual(z.numpy(), np.ones([2, 3]))
z = array_ops.ones(array_ops.shape(d))
self.assertEqual(z.dtype, dtypes_lib.float32)
self.assertEqual([2, 3], z.get_shape())
self.assertAllEqual(z.numpy(), np.ones([2, 3]))
# Test explicit type control
for dtype in (dtypes_lib.float32, dtypes_lib.float64, dtypes_lib.int32,
              dtypes_lib.uint8, dtypes_lib.int16, dtypes_lib.int8,
              dtypes_lib.complex64, dtypes_lib.complex128, dtypes_lib.int64,
              dtypes_lib.bool):
    z = array_ops.ones([2, 3], dtype=dtype)
    self.assertEqual(z.dtype, dtype)
    self.assertEqual([2, 3], z.get_shape())
    self.assertAllEqual(z.numpy(), np.ones([2, 3]))
    z = array_ops.ones(array_ops.shape(d), dtype=dtype)
    self.assertEqual(z.dtype, dtype)
    self.assertEqual([2, 3], z.get_shape())
    self.assertAllEqual(z.numpy(), np.ones([2, 3]))
