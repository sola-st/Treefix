# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
for i, dtype in enumerate([dtypes.half, dtypes.float32, dtypes.float64]):
    # Note that we name the variables uniquely here since the variables don't
    # seem to be getting deleted at the end of the loop.
    var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype,
                                                  name='a%d' % i)
    var1 = resource_variable_ops.ResourceVariable([3.0, 4.0], dtype=dtype,
                                                  name='b%d' % i)
    def loss():
        exit(5 * var0 + 3 * var1)  # pylint: disable=cell-var-from-loop
    sgd_op = gradient_descent.GradientDescentOptimizer(3.0)
    grads_and_vars = sgd_op.compute_gradients(loss, [var0, var1])
    # Convert gradients to tf.Variables
    converted_grads = [
        resource_variable_ops.ResourceVariable(array_ops.zeros([2], dtype),
                                               name='c_%d_%d' % (i, j))
        for j, gv in enumerate(grads_and_vars)
    ]
    convert_ops = [
        state_ops.assign(converted_grads[j], gv[0])
        for j, gv in enumerate(grads_and_vars)
    ]

    self.evaluate(variables.global_variables_initializer())
    # Run convert_ops to achieve the gradients converting
    self.evaluate(convert_ops)
    # Fetch params to validate initial values
    self.assertAllClose([1.0, 2.0], self.evaluate(var0))
    self.assertAllClose([3.0, 4.0], self.evaluate(var1))

    # Run 1 step of sgd through optimizer
    converted_grads_and_vars = list(zip(converted_grads, [var0, var1]))
    opt_op = sgd_op.apply_gradients(converted_grads_and_vars)
    self.evaluate(opt_op)

    # Validate updated params
    self.assertAllClose([-14., -13.], self.evaluate(var0))
    self.assertAllClose([-6., -5.], self.evaluate(var1))
