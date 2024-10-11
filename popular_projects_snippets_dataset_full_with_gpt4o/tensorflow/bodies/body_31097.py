# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
x_val = np.random.random_sample(x_shape).astype(np.float32)
f_val = np.random.random_sample(f_shape).astype(np.float32)
x = constant_op.constant(x_val, name="x", dtype=dtypes.float32)
f = constant_op.constant(f_val, name="f", dtype=dtypes.float32)
output = nn_ops.convolution(
    input=x, filter=f, dilation_rate=dilation_rate, padding=padding)
y_shape = output.get_shape().as_list()
err = gradient_checker.compute_gradient_error([x, f], [x_shape, f_shape],
                                              output, y_shape)
err_tolerance = 1e-2
self.assertLess(err, err_tolerance)
