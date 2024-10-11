# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for dtype in [np.complex64, np.complex128, np.clongdouble]:
    x = np.array([1.5, 2.5 + 2.j, 3.5], dtype=dtype)
    y_np = x.astype(np.float32)
    y_tf = x.astype(float_type)
    numpy_assert_allclose(y_np, y_tf, atol=2e-2, float_type=float_type)

    z_np = y_np.astype(dtype)
    z_tf = y_tf.astype(dtype)
    numpy_assert_allclose(z_np, z_tf, atol=2e-2, float_type=float_type)
