# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
for i, dtype in enumerate([dtypes.half, dtypes.float32, dtypes.float64]):
    # Note that we name the variables uniquely here since the variables don't
    # seem to be getting deleted at the end of the loop.
    var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype,
                                                  name='a_%d' % i)
    var1 = resource_variable_ops.ResourceVariable([3.0, 4.0], dtype=dtype,
                                                  name='b_%d' % i)
    sgd_op = gradient_descent.GradientDescentOptimizer(3.0)
    with self.assertRaisesRegex(ValueError,
                                'No gradients provided for any variable'):
        sgd_op.apply_gradients([(None, var0), (None, var1)])
