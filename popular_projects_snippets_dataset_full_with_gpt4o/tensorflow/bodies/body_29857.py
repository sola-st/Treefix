# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session(use_gpu=use_gpu):
    # Creates a tensor of non-zero values with shape 2 x 3.
    # NOTE(kearnes): The default numpy dtype associated with tf.string is
    # np.object_ (and can't be changed without breaking a lot things), which
    # causes a TypeError in constant_op.constant below. Here we catch the
    # special case of tf.string and set the numpy dtype appropriately.
    if dtype == dtypes_lib.string:
        numpy_dtype = np.string_
    else:
        numpy_dtype = dtype.as_numpy_dtype
    if fully_defined_shape:
        d = constant_op.constant(
            np.ones((2, 3), dtype=numpy_dtype), dtype=dtype)
    else:
        d = array_ops.placeholder(dtype=dtype)
    # Constructs a tensor of zeros of the same dimensions and type as "d".
    z_var = array_ops.zeros_like(d)
    # Test that the type is correct
    self.assertEqual(z_var.dtype, dtype)
    # Test that the shape is correct
    if fully_defined_shape:
        self.assertEqual([2, 3], z_var.get_shape())

    # Test that the value is correct
    feed_dict = {}
    if not fully_defined_shape:
        feed_dict[d] = np.ones((2, 3), dtype=numpy_dtype)
    z_value = z_var.eval(feed_dict=feed_dict)
    self.assertFalse(np.any(z_value))
    self.assertEqual((2, 3), z_value.shape)
