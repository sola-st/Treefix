# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
constraint_01 = lambda x: clip_ops.clip_by_value(x, -0.1, 0.)
constraint_0 = lambda x: clip_ops.clip_by_value(x, 0., 1.)
with self.cached_session():
    var0 = variables.Variable([1.0, 2.0],
                              constraint=constraint_01)
    var1 = variables.Variable([3.0, 4.0],
                              constraint=constraint_0)
    cost = 5 * var0 + 3 * var1
    global_step = variables.Variable(
        array_ops.zeros([], dtypes.int64), name='global_step')
    sgd_op = gradient_descent.GradientDescentOptimizer(3.0)
    opt_op = sgd_op.minimize(cost, global_step, [var0, var1])

    self.evaluate(variables.global_variables_initializer())
    # Fetch params to validate initial values
    self.assertAllClose([1.0, 2.0], self.evaluate(var0))
    self.assertAllClose([3.0, 4.0], self.evaluate(var1))
    # Run 1 step of sgd through optimizer
    opt_op.run()
    # Validate updated params
    self.assertAllClose([-0.1, -0.1], self.evaluate(var0))
    self.assertAllClose([0., 0.], self.evaluate(var1))
