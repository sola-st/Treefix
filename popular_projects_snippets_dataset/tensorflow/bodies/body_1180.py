# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv3d_test.py
x_shape = [2, 3, 4, 3, 2]
f_shape = [3, 3, 3, 2, 2]
y_shape = [2, 6, 8, 6, 2]
strides = [1, 2, 2, 2, 1]
np.random.seed(1)  # Make it reproducible.
x_val = np.random.random_sample(x_shape).astype(np.float64)
f_val = np.random.random_sample(f_shape).astype(np.float64)
with self.session(), self.test_scope():
    x = constant_op.constant(x_val, name="x", dtype=dtypes.float32)
    f = constant_op.constant(f_val, name="f", dtype=dtypes.float32)
    output = nn_ops.conv3d_transpose(
        x, f, y_shape, strides=strides, padding="SAME")
    err = gradient_checker.compute_gradient_error([x, f], [x_shape, f_shape],
                                                  output, y_shape)
print("conv3d_transpose gradient err = %g " % err)
err_tolerance = 0.001
self.assertLess(err, err_tolerance)
