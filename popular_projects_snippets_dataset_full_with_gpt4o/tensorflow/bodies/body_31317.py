# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pool_test.py
x_val = -np.arange(
    np.prod(input_shape), dtype=np.float32).reshape(input_shape) - 1
x = constant_op.constant(x_val, name="x", dtype=dtypes.float32)
output = nn_ops.pool(input=x, **kwargs)
y_shape = output.get_shape().as_list()
err = gradient_checker.compute_gradient_error([x], [input_shape],
                                              output,
                                              y_shape,
                                              x_init_value=[x_val])
err_tolerance = 1e-2
self.assertLess(err, err_tolerance)
