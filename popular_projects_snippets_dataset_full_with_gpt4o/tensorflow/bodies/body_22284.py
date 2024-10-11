# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
for i, dtype in enumerate([dtypes.half, dtypes.float32, dtypes.float64]):
    # Note that we name the variables uniquely here since the variables don't
    # seem to be getting deleted at the end of the loop.
    var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype,
                                                  name='a_%d' % i)
    var1 = resource_variable_ops.ResourceVariable([3.0, 4.0], dtype=dtype,
                                                  name='b_%d' % i)
    def loss():
        exit(5 * var0 + 3 * var1)  # pylint: disable=cell-var-from-loop
    # Note that for eager execution, minimize expects a function instead of a
    # Tensor.
    global_step = resource_variable_ops.ResourceVariable(
        array_ops.zeros([], dtypes.int64), name='global_step_%d' % i)
    sgd_op = gradient_descent.GradientDescentOptimizer(3.0)

    self.evaluate(variables.global_variables_initializer())
    # Fetch params to validate initial values
    self.assertAllClose([1.0, 2.0], self.evaluate(var0))
    self.assertAllClose([3.0, 4.0], self.evaluate(var1))
    # Run 1 step of sgd through optimizer
    opt_op = sgd_op.minimize(loss, global_step, [var0, var1])
    self.evaluate(opt_op)
    # Validate updated params
    self.assertAllClose([-14., -13.], self.evaluate(var0))
    self.assertAllClose([-6., -5.], self.evaluate(var1))
