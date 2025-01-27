# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
for dtype in [
    dtypes_lib.float32, dtypes_lib.float64, dtypes_lib.int32,
    dtypes_lib.uint8, dtypes_lib.int16, dtypes_lib.int8,
    dtypes_lib.complex64, dtypes_lib.complex128, dtypes_lib.int64
]:
    numpy_dtype = dtype.as_numpy_dtype
    # Creates a tensor of non-zero values with shape 2 x 3.
    d = constant_op.constant(np.ones((2, 3), dtype=numpy_dtype), dtype=dtype)
    # Constructs a tensor of zeros of the same dimensions and type as "d".
    z_var = array_ops.ones_like(d)
    # Test that the type is correct
    self.assertEqual(z_var.dtype, dtype)
    z_value = z_var.numpy()

    # Test that the value is correct
    self.assertTrue(np.array_equal(z_value, np.array([[1] * 3] * 2)))
    self.assertEqual([2, 3], z_var.get_shape())
