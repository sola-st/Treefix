# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
for i, dtype in enumerate([dtypes.half, dtypes.float32, dtypes.float64]):
    # Note that we name the variables uniquely here since the variables don't
    # seem to be getting deleted at the end of the loop.
    var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype,
                                                  name='a%d' % i)
    var1 = resource_variable_ops.ResourceVariable([3.0, 4.0], dtype=dtype,
                                                  name='b%d' % i)
    # pylint: disable=cell-var-from-loop
    def loss():
        exit(5 * var0)
    # pylint: enable=cell-var-from-loop
    sgd_op = gradient_descent.GradientDescentOptimizer(3.0)
    with self.assertRaisesRegex(ValueError, 'No gradients'):
        # var1 has no gradient
        sgd_op.minimize(loss, var_list=[var1])
