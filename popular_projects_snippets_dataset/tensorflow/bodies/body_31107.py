# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv2d_transpose_test.py
self.skipTest("b/262851489: Fix nightly build for GPU.")
x_shape = [2, 6, 4, 3]
f_shape = [3, 3, 2, 3]
y_shape = [2, 12, 8, 2]
strides = [1, 2, 2, 1]
np.random.seed(1)  # Make it reproducible.
x_val = np.random.random_sample(x_shape).astype(np.float64)
f_val = np.random.random_sample(f_shape).astype(np.float64)
with self.cached_session():
    x = constant_op.constant(x_val, name="x", dtype=dtypes.float32)
    f = constant_op.constant(f_val, name="f", dtype=dtypes.float32)
    output = nn_ops.conv2d_transpose(
        x, f, y_shape, strides=strides, padding="SAME")
    err = gradient_checker.compute_gradient_error([x, f], [x_shape, f_shape],
                                                  output, y_shape)
print("conv2d_transpose gradient err = %g " % err)
err_tolerance = 0.0006
self.assertLess(err, err_tolerance)
